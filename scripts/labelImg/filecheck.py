# -*- coding: utf-8 -*-
#
# Usage: $ Python filecheck.py image_folder
# 
import sys
import glob
import os

# メイン
def main():
    # 引数１から画像フォルダ名取得
    args = sys.argv
    if (len(args) != 2):
        print("Usage: $ python" + args[0] + " folder name")
        quit()

    folder_name = args[1]
    # print("Folder name (args[1]) is %s" % folder_name)

    print("----- *.jpg")
    # 存在するアノテーションファイル(*.txt)一覧の取得
    for file_name in glob.glob('./%s/*.txt' % folder_name):
        # print("File name is %s" % file_name)

        # ファイル名と拡張子を取得
        name_base, name_ext = os.path.splitext(file_name)
        if not os.path.isfile('./' + name_base + '.jpg'):
            print(name_base + '.jpg' + " が存在しません")

    print("----- *.txt")
    # 存在する画像ファイル(*.jpg)一覧の取得
    for image_file in glob.glob('./%s/*.jpg' % folder_name):
        # print("Image File name is %s" % image_file)

        # ファイル名と拡張子を取得
        name_base, name_ext = os.path.splitext(image_file)
        if not os.path.isfile('./' + name_base + '.txt'):
            print(name_base + '.txt' + " が存在しません")

if __name__ == '__main__':
	main()

print("----- Done!")
