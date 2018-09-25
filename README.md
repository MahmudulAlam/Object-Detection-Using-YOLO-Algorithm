# Object Detection Using YOLO Algorithm
YOLO is a state-of-the-art object detection and classification algorithm which stands for "You Only Look Once". It is extremely fast and thus real-time object detection is possible. "Only Look Once" in the algorithm means it requires only one forward propagation pass through the network to make predictions of object classes and bounding boxes.

## Requirements
- [x] TensorFlow
- [x] OpenCV
- [x] Darkflow
- [x] yolov2.weights : Download the file and put in a bin folder in the working directory (working directory/bin/yolov2.weights).

[![Download](https://img.shields.io/badge/download-yolov2.weights-brightgreen.svg?longCache=true&style=flat)](https://pjreddie.com/media/files/yolov2.weights)

Originally YOLO is written in C and Darknet. Darknet is a neural network library for C. However, the TensorFlow implementation of Darknet, Darkflow and Python has been used here.

## Outputs
This is how the outputs of YOLO look like.

<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/40066164-596cd560-5885-11e8-858e-850c1f8883f8.jpg" width="700">
</p>


<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/45701659-a7858e80-bb91-11e8-828e-bf3949d1b9f0.jpg" width="700">
</p>

## References
- [YOLO](https://pjreddie.com/darknet/yolov2/) Real-Time Object Detection.
- [Darkflow](https://github.com/thtrieu/darkflow) TensorFlow Implementation of Darknet.
