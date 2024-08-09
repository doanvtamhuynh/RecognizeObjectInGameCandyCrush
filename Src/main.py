import cv2
import os
import numpy as np

path = os.path.abspath(os.path.join(os.getcwd(),'..')) + '/Video/videotestcandycrush.mp4'
cap = cv2.VideoCapture(path)

output_width = 800
output_height = 600

while True:
    _, frame = cap.read()





    resized_frame = cv2.resize(frame, (output_width, output_height))
    cv2.imshow("Candy Crush", resized_frame)

    if cv2.waitKey(100) & 0xff == 27:
        break