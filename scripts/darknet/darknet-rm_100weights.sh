#! /bin/bash

# *100.weights ～ *900.weights ファイルを削除する
# Usage: ./darknet-rm_100weights.sh [モデルのフォルダ名]
# $ ./darknet-rm_100weights.sh pp4

if ["$1" = ""]
then
	echo ""
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/darknet"
	echo "$ source activate tensorflow"
	echo "$ ./darknet-rm_100weights.sh [weights folder name]"
	echo "e.g."
	echo "$ ./darknet-rm_100weights.sh pp4"
	echo ""
	exit 1
fi

TRIAL=$1

rm backup/$TRIAL/*[1-9]00.weights
exit 0
