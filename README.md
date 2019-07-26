# ごみ分別スマホアプリ

**ごみ検出イメージです**
***動画***
<a href="https://www.youtube.com/watch?v=NQ57sMHpjRg&feature=youtu.be"><img src="sample/movie.png" alt="movie" width="180" height="280"/></a>

***静止画***
![pp](sample/★PPバンド2.png), ![cell](sample/★乾電池+ボタン電池+粘着テープ2.png)

![tape](sample/★粘着テープとボタン電池2.png), ![tape](sample/★粘着テープ茶+乾電池+ボタン電池2.png)

![ごみ3](sample/c-remocon2-A.png), ![ごみ4](sample/e-remocon-A.png)

![ごみ2](sample/leather2-A.png), ![ごみ5](sample/work3-A.png)

![ごみ1](sample/marker2-A.png), 

**APKファイルは[こちら](https://github.com/keides2/android-yolo-v2/blob/master/release/garbage-release.apk)からダウンロードできます**

<a href="https://github.com/keides2/android-yolo-v2/blob/master/release/garbage-release.apk" download><img src="sample/ic_launcher.png"></a>

※ 検出できるごみは、下のファイルに記載の物になります。

https://github.com/keides2/android-yolo-v2/blob/master/assets/tiny-yolo-voc-labels.txt

**-----**

**以下は、ベースとなった Zoltán Szabó さんの README です。**
https://github.com/szaza/android-yolo-v2

# Android YOLO with TensorFlow Mobile
This android application uses YOLOv2 model for object detection. It uses tensorflow mobile to run neural networks. I would like to use tensorflow lite later. Probably, it is the first open source implementation of the second version of YOLO for Tensorflow on Android device. The demo application detects 20 classes of Pascal VOC dataset. Please read this paper for more information about the YOLOv2 model: [YOLO9000 Better, Faster, Stronger](https://arxiv.org/pdf/1612.08242.pdf).

**Train YOLO for your own dataset**

Please find more information about retraining the model on my site: https://sites.google.com/view/tensorflow-example-java-api/complete-guide-to-train-yolo. I've also added several Google Colab interactive sample for the step-by-step tutorial, so the training process can be tried out on Google virtual machines.

**Steps to compile and run the application:**

Prerequirements:

* Install the [Android Studio](https://developer.android.com/studio/index.html);
* Android 6.0 (API level 23) or higher is required to run the demo application due to usage of Camera2 API;

Compile and run the project:

* Clone this repository with command: `git clone https://github.com/szaza/android-yolo-v2.git`;
* Imort your project into the Android Studio;
* Optional: put your protobuff file and labels.txt into the assets folder, then change the settings properly in the [Config.java](https://github.com/szaza/android-yolo-v2/blob/master/src/org/tensorflow/yolo/Config.java) file;
* Run the project from Android Studio;

How it works?

![android yolo v2 sample image](sample/android-yolo-v2.png)
![android yolo v2 sample image](sample/android-yolo-v2.1.png)

If you would like a more accurate solution, create a server application. See my related projects here:
* [Tensorflow Example Java API](https://sites.google.com/view/tensorflow-example-java-api/home)
* [Tensorflow Java example server application with YOLOv2 model](https://sites.google.com/view/tensorflow-example-java-api/tensorflow-java-api-with-spring-framework)
