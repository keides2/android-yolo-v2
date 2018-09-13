#!/bin/bash

# 秘伝のたれを使って、学習する
# Usage: ./darknet-train.sh [秘伝のたれファイル名] [作成するモデルのフォルダ名]
# $ ./darknet-train.sh pp2/pp2_final.weights pp4


# if ["$1" = ""]
if [ $# -ne 2 ]
then
	echo ""
	echo "This script needs 2 parameters."
	echo "Usage:"
	echo "$ cd ~/darknet"
	echo "$ source activate tensorflow"
	echo "$ ./darknet-train.sh [path to pre-trained weights file] [weights folder name]"
	echo "e.g."
	echo "$ ./darknet-train.sh pp2/pp2_final.weights pp4"
	echo ""
	exit 1
fi

WEIGHTS=$1	# pre-trained weights
TRIAL=$2	# weights folder name

mkdir $TRIAL
./darknet detector train \
cfg/$TRIAL/$TRIAL.data \
cfg/$TRIAL/$TRIAL.cfg \
# bin/darknet19_448.conv.23
backup/$WEIGHTS \
1>> backup/$TRIAL'-'train.log 

echo "Done!"
exit 0
