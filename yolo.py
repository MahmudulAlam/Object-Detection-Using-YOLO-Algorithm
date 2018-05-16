import cv2
import time
import numpy as np
from darkflow.net.build import TFNet

options = {'model': 'cfg/yolo.cfg',
           'load': 'bin/yolov2.weights',
           'threshold': 0.3,
           'gpu': 0.7}

tfnet = TFNet(options)

def yolo_solo(file_name):
    image_file = cv2.imread('images/' + file_name)
    output = tfnet.return_predict(image_file)

    for prediction in output:
        label = prediction['label']
        confidence = prediction['confidence']
        tl = (prediction['topleft']['x'], prediction['topleft']['y'])
        br = (prediction['bottomright']['x'], prediction['bottomright']['y'])
        color = tuple(255 * np.random.rand(3))
        image_file = cv2.rectangle(image_file, tl, br, color, 2)
        font = cv2.FONT_HERSHEY_COMPLEX
        image_file = cv2.putText(image_file, label, (tl[0], tl[1] - 5), font, .7, color, 2)

    output_file = 'output/' + file_name
    cv2.imwrite(output_file, image_file)
    cv2.imshow('YOLO: You Only Look Once', image_file)
    cv2.waitKey(0)
    return image_file


def yolo_real_time():
    cam = cv2.VideoCapture(0)
    while True:
        tic = time.time()
        ret, frame = cam.read()
        output = tfnet.return_predict(frame)
        for prediction in output:
            label = prediction['label']
            confidence = prediction['confidence']
            tl = (prediction['topleft']['x'], prediction['topleft']['y'])
            br = (prediction['bottomright']['x'], prediction['bottomright']['y'])
            color = tuple(255 * np.random.rand(3))
            frame = cv2.rectangle(frame, tl, br, color, 2)
            font = cv2.FONT_HERSHEY_COMPLEX
            frame = cv2.putText(frame, label, tl, font, .7, color, 2)
        cv2.imshow('YOLO in real time', frame)
        toc = time.time()
        print('FPS:' + '{0:.2f}'.format(1 / (toc - tic)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


""" YOLO for single image """
file_name = 'dog.jpg'
#yolo_solo(file_name)

""" YOLO for real time """
yolo_real_time()

print('All Done!')
