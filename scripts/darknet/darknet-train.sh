#!/bin/bash

# 秘伝のたれ/事前学習済みモデルを使って、学習する
# Usage: ./darknet-train.sh [秘伝のたれファイル名] [作成するモデルのフォルダ名]
# $ ./darknet-train.sh backup/pp2/pp2_final.weights pp4
# $ ./darknet-train.sh bin/darknet19_448.conv.23 all


# if ["$1" = ""]
if [[ $# -ne 2 ]]
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

# $TRIALディレクトリが無ければ作成します
echo $TRIAL"ディレクトリが無ければ作成します"
mkdir -p backup/$TRIAL

# 学習開始
echo "学習を開始します"
./darknet detector train \
cfg/$TRIAL/$TRIAL.data \
cfg/$TRIAL/$TRIAL.cfg \
$WEIGHTS \
1>> backup/$TRIAL'-'train.log 
echo "Training done!"

# weights ファイルの移動
mv backup/*.weights backup/$TRIAL
mv backup/*.log backup/$TRIAL

exit 0
