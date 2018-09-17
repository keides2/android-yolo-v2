#!/bin/bash

# labelImg 実行後に、[ファイル名]で始まるtxtファイルの先頭1文字を新しい分類番号に置き換える
# 9分類まで　（1桁のみ対応）
# Usage: ./replace_classid.sh [フォルダ名] [ファイル名] [変更後の分類番号]
# $ ./replace_classid.sh cd 2

if [ $# -ne 3 ]
then
	echo "------------------------------------"
	echo "This script needs 3 parameters."
	echo "Usage:"
	echo "$ cd ~/labelImg/data"
	echo "$ ./replace_classid.sh [path to folder] [path to file] [new classid]"
	echo "e.g."
	echo "$ ./replace_classid.sh cd cd_ 2"
	echo "------------------------------------"
	exit 1
fi

FOLDER=$1
FILE=$2
NEW_CLASSID=$3

sed -i -e 's/^. /'$NEW_CLASSID' /g' $FOLDER'/'$FILE*.txt
exit 0

# 0 button-battery
# 1 tape-all
# 2 cell-battery
# 3 pp-band
# 4 tiewrap-white
# 5 tiewrap-others
# 6 tape-paper
# 7 tape-cloth
# 8 tape-curing
# 9 tape-vinyl
