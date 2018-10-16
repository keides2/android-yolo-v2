#! -*- coding: utf-8 -*-
# $ pip install opencv-python
# $ pip install pillow
import cv2
import numpy as np
import sys
import os
import subprocess

# command
def cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stdout, stderr = p.communicate()
    return stdout.rstrip()

# メイン
def main():
    # データ保存場所
    backup_dir = './model'

    # Linux
    # print("cmd: ls ./image_data")
    # dirs = cmd("ls "+"./image_data")

    # Windows
    # $ cd ./Documents
    print("cmd: dir ./image_data")
    dirs = cmd('dir .' + os.path.sep + 'image_data')
    print("dirs: %s" % dirs)

    # directory separater in both Linux and Windows
    # path = os.path.join('Documents', 'image_data')
    # or
    # path = 'Documents' + os.path.sep + 'image_data'
    # path = "C:/documents/nori/tama".replace('/', os.sep)

    labels = dirs.splitlines()
    print("labels: %s" % labels)

    if os.path.exists(backup_dir):
        # Linux
        # print("cmd: rm -rf backup_dir")
        # cmd("rm  -rf "+backup_dir)

        # Windows
        print("cmd: del /q backup_dir")
        cmd("del /q "+backup_dir)

    # make directories
    os.makedirs(backup_dir)
    labelsTxt_backup = open(backup_dir + '/labels.txt','w')
    classNo=0
    for label in labels:
        labelsTxt_backup.write(label.decode('utf-8')+"\n")
        classNo += 1

    NUM_CLASSES = classNo
    print("class number=" + str(NUM_CLASSES))
    labelsTxt_backup.close()

'''
# ヒストグラム均一化
def equalizeHistRGB(src):
    RGB = cv2.split(src)
    Blue   = RGB[0]
    Green = RGB[1]
    Red    = RGB[2]
    for i in range(3):
        cv2.equalizeHist(RGB[i])
    img_hist = cv2.merge([RGB[0],RGB[1], RGB[2]])
    return img_hist

# ガウシアンノイズ
def addGaussianNoise(src):
    row,col,ch= src.shape
    mean = 0
    var = 0.1
    sigma = 15
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = src + gauss
    return noisy

# salt&pepperノイズ
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

# N増し
# 画像ファイルパスのリスト生成
labels = []
with open(backup_dir + '/labels.txt','r') as f:
    for line in f:
        labels.append(line.rstrip())
print("labels: %s" % labels)

image_file_names = []

for label in labels:
    image_dirs = cmd('ls '+'./image_data/' + label).decode('utf-8')
    image_files = image_dirs.splitlines()
    for image_file in image_files:
        image_file_names.append('./image_data/' + label + '/' + image_file)
print(image_file_names)

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

for image_file in image_file_names:
    # 画像の読み込み
    img_src = cv2.imread(image_file, 1)
    trans_img = []
    trans_img.append(img_src)

    # LUT変換
    for i, LUT in enumerate(LUTs):
        trans_img.append(cv2.LUT(img_src, LUT))

    # 平滑化
    trans_img.append(cv2.blur(img_src, average_square))

    # ヒストグラム均一化
    trans_img.append(equalizeHistRGB(img_src))

    # ノイズ付加
    trans_img.append(addGaussianNoise(img_src))
    trans_img.append(addSaltPepperNoise(img_src))

    # 反転
    flip_img = []
    for img in trans_img:
        flip_img.append(cv2.flip(img, 1))
    trans_img.extend(flip_img)

    dir_name =  os.path.splitext(os.path.dirname(image_file))[0]
    base_name =  os.path.splitext(os.path.basename(image_file))[0]
    img_src.astype(np.float64)
  
    for i, img in enumerate(trans_img):
        if i > 0:
            cv2.imwrite(dir_name + '/trans_' + base_name + '_' + str(i-1) + '.jpg' ,img)
            
'''
if __name__ == '__main__':
	main()

print("Done!")
