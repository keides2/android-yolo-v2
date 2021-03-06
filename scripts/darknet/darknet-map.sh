#!/bin/bash

# weightsファイルから、mAPを計算する
# Usage: ./darknet-map.sh [モデルのフォルダ名]
# $ ./darknet-map.sh pp4

if [[ $1 = "" ]]
then
	echo ""
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/darknet"
	echo "$ source activate tensorflow"
	echo "$ ./darknet-map.sh [weights folder name]"
	echo "e.g."
	echo "$ ./darknet-map.sh pp4"
	echo ""
	exit 1
fi

start_value=1000	# 最初=1000から
stop_value=41000	# 最後=40000（+1000）

TRIAL=$1
FILE_NAME=$TRIAL-map_result.txt

# 繰り返すときは、$TRIAL-map_result.txtを削除してからリスタート
if [ -e backup/$TRIAL/$FILE_NAME ]
then
	echo $FILE_NAME" が存在するので、削除します"
	rm backup/$TRIAL/$FILE_NAME
fi

# .weightsファイルを移動する
echo $TRIAL" フォルダを作成します"
mkdir -p backup/$TRIAL
echo "すべての .weightsファイルを "$TRIAL" フォルダに移動します"
mv backup/*.weights backup/$TRIAL

# mAP計算開始
echo "mAPを計算します"
for ((i=start_value; i<stop_value; i+=1000))
do
	echo $TRIAL'_'${i}
	echo $TRIAL'_'${i} >> backup/$TRIAL/$FILE_NAME
	echo '---------------------------' >> backup/$TRIAL/$FILE_NAME
	./darknet detector map cfg/$TRIAL/$TRIAL.data \
	cfg/$TRIAL/$TRIAL.cfg \
	backup/$TRIAL/$TRIAL'_'${i}.weights >> backup/$TRIAL/$FILE_NAME
	echo ' ' >> backup/$TRIAL/$FILE_NAME
done
echo "Done!"
exit 0

