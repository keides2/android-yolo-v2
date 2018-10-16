#! -*- coding: utf-8 -*-
import sys
import os
from PIL import Image
import cv2
import numpy as np

# メイン
def main():
    # 引数１から画像ファイル名取得
    args = sys.argv
    if (len(args) != 2):
        print("Usage: $ python " + args[0] + " sample.jpg")
        quit()

    file_path = args[1]
    print("File path (args[1]) is %s" % file_path)

    ############################
    # PIL による open～save
    ############################
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

    # 回転しないで保存する新しいファイル名の準備
    ftitle, fext = os.path.splitext(file_path)

    # <1>
    # Exif なしでファイル保存
    # Exif 情報を反映するフォトビューアーと同じ画像を保存
    # Exif の向き情報（Orientation）なし
    new_file_path = ftitle + '-orient-' + str(orientation) + '_PIL' + fext

    # print("New File path is %s" % new_file_path)
    img.save(new_file_path, 'JPEG')
    print("<1> %s を保存しました" % new_file_path)

    # <2>
    # Exif つきでファイル保存
    # Exif 情報を反映しない Chrome と同じ画像を保存
    # Exif の向き情報（Orientation）あり
    exif = img.info['exif']
    new_file_path = ftitle + '-orient-' + str(orientation) + '_PIL+Exif' + fext
    img.save(new_file_path, 'JPEG', exif=exif)
    print("<2> %s を保存しました" % new_file_path)

    ############################
    # OpenCV による open～save
    ############################
    # <3>
    # Exif 無視でオープン
    # Exif 情報を反映するフォトビューアーと同じ向きでオープン
    img = cv2.imread(file_path, cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)
    cv2.imshow(file_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存
    # Exif の向き情報（Orientation）なし
    new_file_path = ftitle + '-orient-' + str(orientation) + '_CV2' + fext
    cv2.imwrite(new_file_path ,img)
    print("<3> %s を保存しました" % new_file_path)

    # <4>
    # Exif 反映してオープン
    # Exif 情報を反映しない Chrome と同じ向きでオープン
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)
    cv2.imshow(file_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 保存
    # Exif の向き情報（Orientation）なし
    new_file_path = ftitle + '-orient-' + str(orientation) + '_CV2+Exif' + fext
    cv2.imwrite(new_file_path ,img)
    print("<4> %s を保存しました" % new_file_path)

if __name__ == '__main__':
	main()

print("Done!")
