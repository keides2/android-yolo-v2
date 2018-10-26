# -*- coding: utf-8 -*-
import glob, os
import sys
import shutil

# 引数１からフォルダ名取得
args = sys.argv
if (len(args) != 3):
    print("Usage: $ python" + args[0] + " <image folder> <ratio of test(%)>")
    quit()

path_data = args[1]
percentage_test = int(args[2])
print("Folder name is '%s'. ratio of test is %d%%." % (path_data, percentage_test))

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
# path_data = 'data/all2/'

# Percentage of images to be used for the test set
# percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
# for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
for pathAndFilename in glob.iglob(os.path.join(path_data, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    # print("title is %s. ext is %s." % (title, ext))

    if counter == index_test:
        counter = 1
        file_test.write(path_data + '/' + title + '.jpg' + '\n')
    else:
        file_train.write(path_data + '/' + title + '.jpg' + '\n')
        counter = counter + 1

file_train.close()  # 閉じないと次に開けない
file_test.close()   # 閉じないと次に開けない

print("(1/2) Done!")

# ファイル移動
dst_dir = path_data + '/test'
print("dst_dir: '%s'" % dst_dir)

if not os.path.exists(dst_dir) :
    os.makedirs(dst_dir)

# 1行抜き出し
file_name = 'test.txt'
print("file_name is '%s'" % file_name)
'''
if not os.path.exists(file_name) :
    print("not exit")
else:
    print("exist")
'''

with open(file_name) as f:
    print("open file")
    '''
    while True:
        s_line = f.readline()
        print(s_line)
        if not s_line:
            break   
    '''
    for line in f:
        print("line: %s" % line)
        print("画像を %s/test へ移動します" % path_data)

        # ファイル名と拡張子を取得
        name_base, name_ext = os.path.splitext(line)
        print("name_base is '%s'" % name_base)
        base_name =  os.path.splitext(os.path.basename(line))[0]
        print(" base_name: %s" % base_name)

        from_file_jpg = name_base + '.jpg'
        from_file_txt = name_base + '.txt'
        print("from_file_jpg is '%s'" % from_file_jpg)

        to_file_jpg = dst_dir + '/' + base_name + '.jpg'
        to_file_txt = dst_dir + '/' + base_name + '.txt'
        print("to_file_jpg is '%s'" % to_file_jpg)
        
        shutil.move(from_file_jpg, to_file_jpg)
        shutil.move(from_file_txt, to_file_txt)

print("(2/2) Done!")





