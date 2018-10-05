#!/bin/bash

# logファイルからlossを抜き出す
# Usage: ./darknet-log_grep.sh [モデルのフォルダ名]
# $ ./darknet-log_grep.sh pp4

if [[ $1 = "" ]]
then
	echo ""
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/darknet"
	echo "$ source activate tensorflow"
	echo "$ ./darknet-log_grep.sh [weights folder name]"
	echo "e.g."
	echo "$ ./darknet-log_grep.sh pp4"
	echo ""
	exit 1
fi

TRIAL=$1
FILE_NAME=$TRIAL'-train'

# 必要な情報を抜き出す
echo "lossを含む行を抜き出します"
grep -e loss backup/$FILE_NAME'.log' > backup/$FILE_NAME'-A.txt'

echo "Done!"
exit 0
