import glob, os
import sys

# 引数１からフォルダ名取得
args = sys.argv
if (len(args) != 3):
    print("Usage: $ python" + args[0] + " <image folder> <ratio of test(%)>")
    quit()

path_data = args[1]
percentage_test = int(args[2])
print("Folder name is '%s'. ratio of test is %d%%." % (path_data, percentage_test))

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
# path_data = 'data/all2/'

# Percentage of images to be used for the test set
# percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
# for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
for pathAndFilename in glob.iglob(os.path.join(path_data, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    # print("title is %s. ext is %s." % (title, ext))

    if counter == index_test:
        counter = 1
        file_test.write(path_data + '/' + title + '.jpg' + "\n")
    else:
        file_train.write(path_data + '/' + title + '.jpg' + "\n")
        counter = counter + 1
    # print("index_test = %d, counter = %d" % (index_test, counter))

file_train.close()
file_test.close()

print("Done!")