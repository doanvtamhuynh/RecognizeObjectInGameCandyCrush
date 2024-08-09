import cv2
import os
import numpy as np
import Color
import Contours

path = os.path.abspath(os.path.join(os.getcwd(),'..')) + '/Video/videotestcandycrush.mp4'
cap = cv2.VideoCapture(path)

output_width = 800
output_height = 600

try:
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Tao mat na cho tung mau 'Mark'
        color = Color.ColorRGB

        mask_red = cv2.inRange(hsv, color.lower_red, color.upper_red)
        mask_green = cv2.inRange(hsv, color.lower_green, color.upper_green)
        mask_blue = cv2.inRange(hsv, color.lower_blue, color.upper_blue)
        mask_yellow = cv2.inRange(hsv, color.lower_yellow, color.upper_yellow)
        mask_orange = cv2.inRange(hsv, color.lower_orange, color.upper_orange)
        mask_purple = cv2.inRange(hsv, color.lower_purple, color.upper_purple)

        # Tìm viền cho từng màu

        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_orange, _ = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_purple, _ = cv2.findContours(mask_purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Vẽ đường viền cho đối tượng

        contours = Contours.ContoursObject

        contours.DrawContour(frame,contours_red,"Red",(0, 0, 255))
        contours.DrawContour(frame,contours_green,"Green",(0, 255, 0))
        contours.DrawContour(frame,contours_blue,"Blue",(255, 0, 0))
        contours.DrawContour(frame,contours_yellow,"Yellow",(0, 255, 255))
        contours.DrawContour(frame,contours_orange,"Orange",(0, 165, 255))
        contours.DrawContour(frame,contours_purple,"Purple",(255, 0, 255))

        resized_frame = cv2.resize(frame, (output_width, output_height))
        cv2.imshow("Candy Crush", resized_frame)

        # Nhan Esc de Thoat
        if cv2.waitKey(100) & 0xff == 27:
            break
except Exception as e:
    print("[INFO] Lỗi. Kiểm tra đường dẫn video.")


cap.release()
cv2.destroyAllWindows()