#! /bin/bash

# mapファイルから必要な業だけを抜き出す
# Usage: ./darknet-map_grep.sh [モデルのフォルダ名]
# $ ./darknet-map_grep.sh pp4

if ["$1" = ""]
then
	echo ""
	echo "This script needs 1 parameter."
	echo "Usage:"
	echo "$ cd ~/darknet"
	echo "$ source activate tensorflow"
	echo "$ ./darknet-map_grep.sh [weights folder name]"
	echo "e.g."
	echo "$ ./darknet-map_grep.sh pp4"
	echo ""
	exit 1
fi

TRIAL=$1
FILE_NAME=$TRIAL-map_result

# mapファイルが、CRを使っているので、これをLFに置き換える
sed -e "s/\r/\n/g" backup/$TRIAL/$FILE_NAME'.txt' > backup/$TRIAL/$FILE_NAME'-A.txt'

# 必要な情報を抜き出す
grep -e pp -e class -e thresh -e mAP backup/$TRIAL/$FILE_NAME'-A.txt' > backup/$TRIAL/$FILE_NAME'-B.txt'

echo "Done!"
exit 0
