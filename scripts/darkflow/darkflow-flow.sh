#!/bin/bash

# 重み係数モデル .weightsファイルを.pbファイルに変換する
# Usage: ./darkflow-flow.sh [モデルのフォルダ名]
# $ ./darkflow-flow.sh pp4

if [[ "$1" = "" ]]
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
echo "(1/9) カレントディレクトリを、darkflowに変更します"
cd ~/darkflow

# $TRIALディレクトリが無ければ作成
echo "(2/9) "$TRIAL" ディレクトリを、作成します"
mkdir -p bin/$TRIAL

# .weightsファイルを、darknetからdarkflowへコピー
echo "(3/9) .weightsファイルを、darknetからdarkflowへコピーします"
cp ~/darknet/backup/$TRIAL/$TRIAL'_final'.weights bin/$TRIAL

# リネーム
echo "(4/9) .weightsファイルの名前を変更します"
mv bin/$TRIAL/$TRIAL'_final'.weights bin/$TRIAL/yolov2-tiny-voc.weights

# .cfgファイルをコピー
echo "(5/9) .cfgファイルを、darknetからdarkflowへコピーします"
cp ~/darknet/cfg/$TRIAL/$TRIAL'.cfg' cfg/yolov2-tiny-voc.cfg

# labels.txt の内容を変更します。 darknetの .namesファイルを、darkflowの labels.txtにコピーします
echo "(6/9) darknetの .namesファイルを、darkflowの labels.txtにコピーします"
cp ~/darknet/cfg/$TRIAL/$TRIAL'.names' labels.txt

# 変換開始
echo "(7/9) .weightsファイルを .pbファイルに変換します"
./flow \
	--model cfg/yolov2-tiny-voc.cfg \
	--load bin/$TRIAL/yolov2-tiny-voc.weights \
	--savepb

# リネーム
echo "(8/9) ファイル名をyolov2-tiny-voc.pbから、tiny-yolo-voc-graph.pbに変更します"
mv built_graph/yolov2-tiny-voc.pb built_graph/tiny-yolo-voc-graph.pb

# $TRIALディレクトリ無ければ作成、ファイル移動
echo "(9/9) darkflow/built_graph/"$TRIAL"ディレクトリを作成し、pbファイルをここに移動します"
mkdir -p built_graph/$TRIAL
mv built_graph/tiny-yolo-voc-graph.pb built_graph/$TRIAL/tiny-yolo-voc-graph.pb
mv built_graph/yolov2-tiny-voc.meta built_graph/$TRIAL/yolov2-tiny-voc.meta

# pbファイルをWindowsのAndroid環境にコピーする
# WinSPを使って、tiny-yolo-voc-graph.pbファイルをG:\Android\Project\garbage\assets\tiny-yolo-voc-graph.pb にダウンロード
echo "Done!"
echo "(Next) WinSPを使って、tiny-yolo-voc-graph.pbファイルをG:\Android\Project\garbage\assets\tiny-yolo-voc-graph.pb にダウンロードしてください"
exit 0
