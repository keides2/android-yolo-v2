#!/bin/bash

# *100.weights ～ *900.weights ファイルを削除する
# Usage: ./darknet-rm_100weights.sh [モデルのフォルダ名]
# $ ./darknet-rm_100weights.sh pp4

if [[ $1 = "" ]]
then
	echo ""
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/darknet"
	echo "$ source activate tensorflow"
	echo "$ ./darknet-rm_100weights.sh [weights folder name]"
	echo "e.g."
	echo "$ ./darknet-rm_100weights.sh backup/pp4"
	echo ""
	exit 1
fi

TRIAL=$1

# .weightsファイルを削除する
echo "100回毎の.weightsファイルを削除します"
cd backup
pwd
rm $TRIAL/*[1-9]00.weights
exit 0
