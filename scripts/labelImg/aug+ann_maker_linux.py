# -*- coding: utf-8 -*-
import sys
import cv2
import glob
import numpy as np
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# アフィン変換
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
    
    if deg == '90':
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

# リサイズ
def resize_img(fname, ratio):
    img = Image.open(fname)
    # img_resize = img.resize((int(img.width * ratio), int(img.height * ratio)))
    img_resize_lanczos = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)

    # ファイル名と拡張子を取得
    name_base, name_ext = os.path.splitext(fname)
    print(name_base)

    # ファイル名を変更して保存
    img_resize_lanczos.save(name_base + '-' + str(ratio) + '.jpg')
    print(name_base + '-' + str(ratio) + '.jpg' + ' is saved.')

# 回転
def rotate_img(fname, deg):
    img = Image.open(fname)
    # 左回転に変換
    deg2 = 360 - int(deg)
    img_rotate = img.rotate(deg2, expand=True, resample=Image.BICUBIC)

    # ファイル名と拡張子を取得
    name_base, name_ext = os.path.splitext(fname)
    print(name_base)

    # ファイル名を変更して保存
    img_rotate.save(name_base + '-' + str(deg) + '.jpg')
    print(name_base + '-' + str(deg) + '.jpg' + ' is saved.')

# メイン
def main():
    # 引数１からフォルダ名取得
    args = sys.argv
    folder_name = args[1]
    print("Folder name is %s" % folder_name)
    '''
    # リサイズ
    # 存在する画像ファイル(*.jpg)一覧の取得
    for file_name in glob.glob('./%s/*.jpg' % folder_name):
        print("File name is %s" % file_name)

        # リサイズ 50%
        resize_img(file_name, 0.5)
    '''
    # 回転
    # 存在する画像ファイル(*.jpg)一覧の取得
    for file_name in glob.glob('./%s/*.jpg' % folder_name):
        print("File name is %s" % file_name)

        # 90°回転（Ralphにあわせて右回転指示）
        rotate_img(file_name, 90)

        # 180°回転（Ralphにあわせて右回転指示）
        rotate_img(file_name, 180)

        # 270°回転（Ralphにあわせて右回転指示）
        rotate_img(file_name, 270)

    # アノテーションファイルの自動生成
    # 存在するアノテーションファイル(*.txt)一覧の取得
    for file_name in glob.glob('./%s/*.txt' % folder_name):
        print("File name is %s" % file_name)

        # ファイル名と拡張子を取得
        name_base, name_ext = os.path.splitext(file_name)

        # 1行抜き出し
        for line in open(file_name, 'r'):
            print("Label name is %s" % file_name)
            print("Image name is %s" % file_name.replace(".txt",".jpg"))
 
            # 画像サイズを知る
            img = cv2.imread(file_name.replace(".txt",".jpg"))
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
            degs = ['90', '180', '270']
            for deg in degs:
                # 変換
                bbox2 = convert_coordinate((x, y), (w,h), deg)
                print(str(class_num), " ".join([str(a) for a in bbox2]))
                print(".")
                
                # 同じ名前に角度を追記してファイル保存
                # name_base, name_ext = os.path.splitext(file_name)
                list_write_file = open(name_base + "-" + deg + ".txt", 'a')
                list_write_file.write(str(class_num) + " " + " ".join([str(a) for a in bbox2]) + "\n")
                list_write_file.close()
# break

if __name__ == '__main__':
	main()

print("Done!")
