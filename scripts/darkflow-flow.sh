#!/bin/bash

# 重み係数モデル .weightsファイルを.pbファイルに変換する
# Usage: ./darkflow-flow.sh [モデルのフォルダ名]
# $ ./darkflow-flow.sh pp4

if ["$1" = ""]
then
	echo ""
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/darkflow"
	echo "$ source activate tensorflow"
	echo "$ ./darkflow-flow.sh [weights folder name]"
	echo "e.g."
	echo "$ ./darkflow-flow.sh pp4"
	echo ""
	exit 1
fi

TRIAL=$1

# カレントディレクトリ変更
cd ~/darkflow

# $TRIALディレクトリ作成
mkdir bin/$TRIAL

# .weightsファイルを、darknetからdarkflowにコピー
echo ".weightsファイルを、darknetからdarkflowにコピーします"
cp ~/darknet/backup/$TRIAL/$TRIAL'_final'.weights bin/$TRIAL

# リネーム
echo "ファイル名を変更します"
mv bin/$TRIAL/$TRIAL'_final'.weights bin/$TRIAL/yolov2-tiny-voc.weights

./flow \
	--model cfg/yolov2-tiny-voc.cfg \
	--load bin/$TRIAL/yolov2-tiny-voc.weights \
	--savepb

# リネーム
echo "ファイル名をyolov2-tiny-voc.pbから、tiny-yolo-voc-graph.pbに変更します"
mv built_graph/yolov2-tiny-voc.pb built_graph/tiny-yolo-voc-graph.pb

# $TRIALディレクトリ作成、ファイル移動
echo "darkflow/built_graph/"$TRIAL"ディレクトリを作成し、pbファイルをそこへ移動します"
mkdir built_graph/$TRIAL
mv built_graph/tiny-yolo-voc-graph.pb built_graph/$TRIAL/tiny-yolo-voc-graph.pb
mv built_graph/yolov2-tiny-voc.meta built_graph/$TRIAL/yolov2-tiny-voc.meta

# pbファイルをWindowsのAndroid環境にコピーする
# WinSPを使って、tiny-yolo-voc-graph.pbファイルをG:\Android\Project\garbage\assets\tiny-yolo-voc-graph.pb にダウンロード
echo "WinSPを使って、tiny-yolo-voc-graph.pbファイルをG:\Android\Project\garbage\assets\tiny-yolo-voc-graph.pb にダウンロードしてください"
echo "Done!"
exit 0
