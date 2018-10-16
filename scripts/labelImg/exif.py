#! -*- coding: utf-8 -*-
import sys
import os
from PIL import Image

# メイン
def main():
    # 引数１から画像ファイル名取得
    args = sys.argv
    if (len(args) != 2):
        print("Usage: $ python " + args[0] + " sample.jpg")
        quit()

    file_path = args[1]
    print("File path (args[1]) is %s" % file_path)

    # Orientation タグ値にしたがった処理
    # PIL における Rotate の角度は反時計回りが正
    convert_image = {
        1: lambda img: img,
        2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),                              # 左右反転
        3: lambda img: img.transpose(Image.ROTATE_180),                                   # 180度回転
        4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),                              # 上下反転
        5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90),  # 左右反転＆反時計回りに90度回転
        6: lambda img: img.transpose(Image.ROTATE_270),                                   # 反時計回りに270度回転
        7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270), # 左右反転＆反時計回りに270度回転
        8: lambda img: img.transpose(Image.ROTATE_90),                                    # 反時計回りに90度回転
    }

    img = Image.open(file_path)
    # img.show()

    # Exif 取得。存在しない場合、空の辞書を返して終了する
    exif = img._getexif()

    # 画像の向き取得
    try:
        orientation = exif.get(0x112, 1)
        print(' Orientation: {0}'.format(orientation))
    except AttributeError:
        print(" img の Exif の Orientation が存在しません")
        return {}

    # 回転後のファイル名準備
    ftitle, fext = os.path.splitext(file_path)
    new_file_path = ftitle + '-orient-' + str(orientation) + fext
    print("New File path is %s" % new_file_path)

    # 回転
    print("回転します")
    new_img = convert_image[orientation](img)
    # new_img.show()

    # ファイル保存
    new_img.save(new_file_path, 'JPEG')
    print("%s を保存しました" % new_file_path)

    try:
        # Exif 取得。存在しない場合、空の辞書を返して終了する
        exif = new_img._getexif()

        # 画像の向き取得
        new_orientation = exif.get(0x112, 1)
        print(' Orientation: {0}'.format(new_orientation))
    except AttributeError:
        print(" New File path の Exif の Orientation が存在しません")
        return {}


if __name__ == '__main__':
	main()

print("Done!")
