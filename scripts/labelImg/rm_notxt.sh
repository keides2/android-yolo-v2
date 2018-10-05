#!/bin/bash

# 画像ファイルが無いアノテーションファイルを削除する
# Usage: ./rm_notxt.sh [ファイル名の接頭語]
# $ ./rm_notxt.sh cd

if [[ $# -ne 1 ]]
then
	echo "------------------------------------"
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/labelImg/data"
	echo "$ ./rm_notxt.sh [head of file name]"
	echo "e.g."
	echo "$ ./rm_notxt.sh cd"
	echo "------------------------------------"
	exit 1
fi

HEAD_FILE=$1

# 移動先フォルダ作成
mkdir -p temp
# ls $HEAD_FILE*.txt

# 存在する.jpgファイルを探し、同じ名前の.txt ファイルとともに tempフォルダに退避する
for file in `ls $HEAD_FILE*.jpg`
do
	echo $file
	mv $file temp/$file
	echo ${file%.*}.txt
	mv ${file%.*}.txt temp/${file%.*}.txt
done

# 残った.txtファイルを手作業で削除する
# rm *.txt

exit 0
