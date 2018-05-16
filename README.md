# Object Detection Using YOLO Algorithm
YOLO is a state-of-the-art object detection and classification algorithm which stands for "You Only Look Once". It is extremely fast and thus real time object detection is possible. "Only Look Once" in the algorithm means it requires only one forward propagation pass through the network to make predictions of object classes and bounding boxes.

## Requirements
- [x] TensorFlow
- [x] OpenCV
- [x] Darkflow

Originally YOLO is written in C and Darknet. Darknet is a neural network library for C. However, the TensorFlow implementation of Darknet, Darkflow and Python has been used here.

## Outputs
This is how the outputs of YOLO looks like.

<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/40066230-7e4580c6-5885-11e8-812d-bdee3a761ad0.jpg">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/40066164-596cd560-5885-11e8-858e-850c1f8883f8.jpg">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/37298971/40066181-64658124-5885-11e8-913e-bf78b2978418.jpg">
</p>

## References
- [YOLO](https://pjreddie.com/darknet/yolo/) Real-Time Object Detection.
- [Darkflow](https://github.com/thtrieu/darkflow) TensorFlow Implementation of Darknet. 
