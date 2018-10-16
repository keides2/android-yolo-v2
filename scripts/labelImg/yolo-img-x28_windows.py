# -*- coding: utf-8 -*-
# $ pip install opencv-python
# $ pip install pillow
# Python3
# Usage: $ Python yolo-img-x28_windows.py image_folder
# 
import sys
import cv2
import glob
import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import shutil
import os
from os import listdir, getcwd
from os.path import join

# バウンディング・ボックスのアフィン変換
def convert_coordinate(box, size, deg):
    print("start convert_rotate function:")
    x = box[0]
    y = box[1]
    w = size[0]
    h = size[1]
    print("deg =", deg)
    print("x =", x)
    print("y =", y)
    print("w =", w)
    print("h =", h)
    
    if deg == '0':
        print("deg = 0")
        x2 = x
        y2 = y
        w2 = w
        h2 = h
    elif deg == '90':
        print("deg = 90")
        x2 = 1 - y
        y2 = x
        w2 = h
        h2 = w
    elif deg == '180':
        print("deg = 180")
        x2 = 1 - x
        y2 = 1 - y
        w2 = w
        h2 = h
    elif deg == '270':
        print("deg = 270")
        x2 = y
        y2 = 1 - x
        w2 = h
        h2 = w
    else:
        print("deg = else")
        x2 = x
        y2 = y
        w2 = w
        h2 = h

    print("deg =", deg)
    print("x2 =", x2)
    print("y2 =", y2)
    print("w2 =", w2)
    print("h2 =", h2)

    return (x2, y2, w2 ,h2)

# 画像のリサイズ（未使用につき未確認）
def resize_img(fname, ratio):
    img = Image.open(fname)
    # img_resize = img.resize((int(img.width * ratio), int(img.height * ratio)))
    img_resize_lanczos = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)

    # ファイル名と拡張子を取得
    name_base, name_ext = os.path.splitext(fname)
    # print(name_base)

    # ファイル名を変更して保存
    img_resize_lanczos.save(name_base + '-' + str(ratio) + '.jpg')
    print(name_base + '-' + str(ratio) + '.jpg' + ' is saved.')

# 画像の回転～新しいファイル名で保存
def rotate_img(fname, deg):
    img = Image.open(fname)
    # 左回転に変換
    deg2 = 360 - int(deg)
    img_rotate = img.rotate(deg2, expand=True, resample=Image.BICUBIC)

    # ファイル名と拡張子を取得
    name_base, name_ext = os.path.splitext(fname)
    # print(name_base)

    # ファイル名を変更して保存
    img_rotate.save(name_base + '-' + str(deg) + '.jpg')
    print(name_base + '-' + str(deg) + '.jpg' + ' is saved.')

# ヒストグラム均一化
def equalizeHistRGB(src):
    RGB = cv2.split(src)
    Blue = RGB[0]
    Green = RGB[1]
    Red = RGB[2]
    for i in range(3):
        cv2.equalizeHist(RGB[i])

    img_hist = cv2.merge([RGB[0],RGB[1], RGB[2]])
    return img_hist

# ガウシアンノイズ（未使用）
def addGaussianNoise(src):
    row,col,ch= src.shape
    mean = 0
    var = 0.1
    sigma = 15
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = src + gauss
    return noisy

# salt & pepperノイズ（未使用）
def addSaltPepperNoise(src):
    row,col,ch = src.shape
    s_vs_p = 0.5
    amount = 0.004
    out = src.copy()
    # Salt mode
    num_salt = np.ceil(amount * src.size * s_vs_p)
    coords = [np.random.randint(0, i-1 , int(num_salt))
        for i in src.shape]
    out[coords[:-1]] = (255,255,255)

    # Pepper mode
    num_pepper = np.ceil(amount* src.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i-1 , int(num_pepper))
        for i in src.shape]
    out[coords[:-1]] = (0,0,0)
    return out

# 画像のExifデータを取り出す
def get_exif_of_image(file):
    im = Image.open(file)

    # Exif データを取得
    # 存在しなければそのまま終了 空の辞書を返す
    try:
        exif = im._getexif()

        # タグIDそのままでは人が読めないのでデコードして
        # テーブルに格納する
        exif_table = {}
        for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                exif_table[tag] = value
    except AttributeError:
        print(" exif が存在しません")
        return {}
        
    print(" exif-orientation: {0}".format(exif_table['Orientation']))
    return exif_table

# ExifテーブルのOrientationの数値から、回転する角度と、ミラー反転するかどうかを取得する
def get_exif_rotation(orientation_num):
    """
    return 回転角度,反転するか(0 1)
    # 参考: https://qiita.com/minodisk/items/b7bab1b3f351f72d534b
    """
    if orientation_num == 1:
        return 0, 0
    if orientation_num == 2:
        return 0, 1
    if orientation_num == 3:	# 元画像は、180度、右に回転している
        return 180, 0
    if orientation_num == 4:
        return 180, 1
    if orientation_num == 5:
        return 270, 1
    if orientation_num == 6:	# 元画像は、90度、右に回転している
        return 270, 0
    if orientation_num == 7:
        return 90, 1
    if orientation_num == 8:	# 元画像は、270度、右に回転している
        return 90, 0
 
# Exif情報を使用して、画像を回転し、新しいファイル名で保存する
def rotate_exif_info(path, to_path):
    print(" Func: rotate_exif_info() is called.")
 
    # to_save_path = to_path + os.path.sep + os.path.basename(path)
    to_save_path = to_path + '/' + os.path.basename(path)
    if os.path.exists(to_path) is False:
        os.makedirs(to_path)
 
    exif = get_exif_of_image(path)
    rotate = 0
    reverse = 0
    if 'Orientation' in exif:
        rotate, reverse = get_exif_rotation(exif['Orientation'])

    img = Image.open(path)
 
    data = img.getdata()
    mode = img.mode
    size = img.size
 
    with Image.new(mode, size) as dst:
        dst.putdata(data)
        if reverse == 1:
            dst = ImageOps.mirror(dst)
        if rotate != 0:
            dst = dst.rotate(rotate, expand=True)
        dst.save(to_save_path)

# メイン
def main():
    # 引数１から画像フォルダ名取得
    args = sys.argv
    if (len(args) != 2):
        print("Usage: $ python" + args[0] + " image")
        quit()

    folder_name = args[1]
    print("Folder name (args[1]) is %s" % folder_name)
	
    # 存在する画像ファイル(*.jpg)一覧の取得
    for file_name in glob.glob('./%s/*.jpg' % folder_name):
        print("File name is %s" % file_name)
        dir_name =  os.path.splitext(os.path.dirname(file_name))[0]
        print(" dir_name: %s" % dir_name)
        base_name =  os.path.splitext(os.path.basename(file_name))[0]
        print(" base_name: %s" % base_name)

    '''
    # リサイズ
    # 存在する画像ファイル(*.jpg)一覧の取得
    for file_name in glob.glob('./%s/*.jpg' % folder_name):
        print("File name is %s" % file_name)

        # リサイズ 50%
        resize_img(file_name, 0.5)
    '''

    # <1> 回転
    print("<1> Start rotation:")
    # 存在する画像ファイル(*.jpg)一覧の取得
    for file_name in glob.glob('./%s/*.jpg' % folder_name):
        print("File name is %s" % file_name)
        
        # 0°回転（Exif削除のために呼び出す
        rotate_img(file_name, 0)

        # 90°回転（Ralphにあわせて右回転指示）
        rotate_img(file_name, 90)

        # 180°回転（Ralphにあわせて右回転指示）
        rotate_img(file_name, 180)

        # 270°回転（Ralphにあわせて右回転指示）
        rotate_img(file_name, 270)
		
    # <2> アノテーションファイルの生成
    print("<2> Start annotation:")
    # 存在するアノテーションファイル(*.txt)一覧の取得
    for file_name in glob.glob('./%s/*.txt' % folder_name):
        print("File name is %s" % file_name)

        # ファイル名と拡張子を取得
        name_base, name_ext = os.path.splitext(file_name)
        print(" name_base: %s" % name_base)
        print(" name_ext: %s" % name_ext)
        base_name =  os.path.splitext(os.path.basename(file_name))[0]
        print(" base_name: %s" % base_name)

        # 1行抜き出し
        for line in open(file_name, 'r'):
            print("Label name is %s" % file_name)
            print("Image name is %s" % file_name.replace(".txt",".jpg"))
 
            # 画像サイズを知る
            img = cv2.imread(file_name.replace(".txt",".jpg"), cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)
            #
            # OpeCV Docs imread()
            # If EXIF information are embedded in the image file, 
            # the EXIF orientation will be taken into account 
            # and thus the image will be rotated accordingly 
            # except if the flag IMREAD_IGNORE_ORIENTATION is passed.
            # 
            # ImreadModes()
            # IMREAD_IGNORE_ORIENTATION: If set, do not rotate the image according to EXIF's orientation flag.

            h, w = img.shape[:2]
            print("h =", h)
            print("w =", w)

            # 分類番号、座標抽出
            l = line.split(" ")
            print(l[0])     # 分類番号
            print(l[1])     # バウンディングボックス x座標
            print(l[2])     # バウンディングボックス y座標
            print(l[3])     # バウンディングボックス 幅 w
            print(l[4])     # バウンディングボックス 高さ h

            # 文字→数値化
            bbox = (int(l[0]), float(l[1]), float(l[2]), float(l[3]), float(l[4]))
            class_num = bbox[0]
            x = bbox[1]
            y = bbox[2]
            w = bbox[3]
            h = bbox[4]
            
            # 座標回転＋平行移動（アフィン変換）
            degs = ['0', '90', '180', '270']
            for deg in degs:
                # 変換
                bbox2 = convert_coordinate((x, y), (w,h), deg)
                print(str(class_num), " ".join([str(a) for a in bbox2]))
                print(".")
                
                # 同じ名前に角度を追記してファイル保存
                # name_base, name_ext = os.path.splitext(file_name)
                # list_write_file = open(name_base + '-' + deg + '.txt', 'a', newline="\n")
                with open(name_base + '-' + deg + '.txt', 'a', newline='\n') as list_write_file:
                    list_write_file.write(str(class_num) + " " + " ".join([str(a) for a in bbox2]) + "\n")
                list_write_file.close()
            
        # オリジナル画像の移動（0度も作成するのでダブル）
        backup_dir = folder_name + '/backup'
        if not os.path.exists(backup_dir) :
            os.makedirs(backup_dir)
            
        print("オリジナル画像を ./backup へ移動します")
        from_file_jpg = name_base + '.jpg'     # file_name
        from_file_txt = name_base + '.txt'
        to_file_jpg = backup_dir + '/' + base_name + '.jpg'
        to_file_txt = backup_dir + '/' + base_name + '.txt'
        shutil.move(from_file_jpg, to_file_jpg)
        shutil.move(from_file_txt, to_file_txt)
    
    # <3> 画像変換
    print("<3> Start conversion:")
    # ルックアップテーブルの生成
    min_table = 50
    max_table = 205
    diff_table = max_table - min_table
    gamma1 = 0.75
    gamma2 = 1.5

    LUT_HC = np.arange(256, dtype = 'uint8' )
    LUT_LC = np.arange(256, dtype = 'uint8' )
    LUT_G1 = np.arange(256, dtype = 'uint8' )
    LUT_G2 = np.arange(256, dtype = 'uint8' )

    LUTs = []

    # 平滑化用
    average_square = (10,10)

    # ハイコントラストLUT作成
    for i in range(0, min_table):
        LUT_HC[i] = 0

    for i in range(min_table, max_table):
        LUT_HC[i] = 255 * (i - min_table) / diff_table

    for i in range(max_table, 255):
        LUT_HC[i] = 255

    # その他LUT作成
    for i in range(256):
        LUT_LC[i] = min_table + i * (diff_table) / 255
        LUT_G1[i] = 255 * pow(float(i) / 255, 1.0 / gamma1)
        LUT_G2[i] = 255 * pow(float(i) / 255, 1.0 / gamma2)

    LUTs.append(LUT_HC)
    LUTs.append(LUT_LC)
    LUTs.append(LUT_G1)
    LUTs.append(LUT_G2)

    # 存在する画像ファイル(*.jpg)一覧の取得
    for image_file in glob.glob('./%s/*.jpg' % folder_name):
        print("Image File name is %s" % image_file)

        # 画像の読み込み
        img_src = cv2.imread(image_file, cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)
        trans_img = []
        trans_img.append(img_src)
        print(" trans_img: 画像の読み込み完")

        # LUT変換
        # file_name_0.jpg ～ file_name_3.jpg 生成
        for i, LUT in enumerate(LUTs):
            print(" LUT i = %d" % i)
            trans_img.append(cv2.LUT(img_src, LUT))
        print(" trans_img: LUT変換完")

        # 平滑化
        # file_name_4.jpg 生成
        trans_img.append(cv2.blur(img_src, average_square))
        print(" trans_img: 平滑完")

        # ヒストグラム均一化
        # file_name_5.jpg 生成
        trans_img.append(equalizeHistRGB(img_src))
        print(" trans_img: ヒストグラム均一化完")

        '''
        # ノイズ付加
        # trans_img.append(addGaussianNoise(img_src))
        # trans_img.append(addSaltPepperNoise(img_src))

        # 反転
        # file_name_6.jpg ～ file_name_12.jpg 生成（左右反転）
        # file_name_13.jpg ～ file_name_19.jpg 生成（上下反転）
        flip_img = []
        for img in trans_img:
            # 左右反転
            flip_img.append(cv2.flip(img, 1))
            # 上下反転
            flip_img.append(cv2.flip(img, 0))

        trans_img.extend(flip_img)
        print("trans_img: 反転完")
        '''
        # print("tran i = {0}".format(trans_img[0]))

        # 変換後の画像保存
        print("Saving:")
        # if not os.path.exists("trans_images"):
        #    os.mkdir("trans_images")
        
        dir_name =  os.path.splitext(os.path.dirname(image_file))[0]
        # print(" dir_name: %s" % dir_name)

        base_name =  os.path.splitext(os.path.basename(image_file))[0]
        # print(" base_name: %s" % base_name)
        
        img_src.astype(np.float64)
  
        for i, img in enumerate(trans_img):
            print(" trans i = %d" % i)
            if i > 0:
                img_name = dir_name + os.path.sep + 'trans_' + base_name + '_' + str(i-1) + '.jpg'
                cv2.imwrite(img_name ,img)
                print(" %s is saved." % img_name)

                # アノテーションファイルのコピー
                src = dir_name + os.path.sep + base_name + '.txt'
                dst = dir_name + os.path.sep + 'trans_' + base_name + '_' + str(i-1) + '.txt' 
                shutil.copyfile(src, dst)
                print(" %s is saved." % dst)
        '''
        # オリジナル画像の移動
        backup_dir = folder_name + '/backup'
        if not os.path.exists(backup_dir) :
            os.makedirs(backup_dir)
        print("オリジナル画像を ./backup へ移動します")
        from_file_jpg = dir_name + os.path.sep + base_name + '.jpg'
        from_file_txt = dir_name + os.path.sep + base_name + '.txt'
        to_file_jpg = backup_dir + '/' + base_name + '.jpg'
        to_file_txt = backup_dir + '/' + base_name + '.txt'
        shutil.move(from_file_jpg, to_file_jpg)
        shutil.move(from_file_txt, to_file_txt)
        '''

# break

if __name__ == '__main__':
	main()

print("Done!")
