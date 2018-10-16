# スクレイピング
# !pip install lxml
import requests
import re
import uuid
from bs4 import BeautifulSoup
import os

word = "カメラ"
images_dir = 'image_data/camera/'

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

url = "https://search.nifty.com/imagesearch/search?select=1&chartype=&q=%s&xargs=2&img.fmt=all&img.imtype=color&img.filteradult=no&img.type=all&img.dimensions=large&start=%s&num=20"
pages = [1,20,40,60,80,100]

numb = 0

for p in pages:
    r = requests.get(url%(word,p))
    soup = BeautifulSoup(r.text,'lxml')
    imgs = soup.find_all('img',src=re.compile('^https://msp.c.yimg.jp/yjimage'))
    for img in imgs:
        print('fetched ' + str(img['src']))
        r = requests.get(img['src'])
        with open(images_dir+str(numb)+str('.jpg'),'wb') as file:
            file.write(r.content)
        numb += 1

# 画像の確認
# !ls image_data/camera
# from IPython.display import Image,display_jpeg
# display_jpeg(Image('image_data/camera/0.jpg'))

# 他の画像
# word = "犬"
# images_dir = 'image_data/dog/'
# 
# word = "猫"
# images_dir = 'image_data/cat/'
# max_image = 60