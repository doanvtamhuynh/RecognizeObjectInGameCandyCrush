import cv2
import os
import numpy as np

path = os.path.abspath(os.path.join(os.getcwd(),'..')) + '/Video/videotestcandycrush.mp4'
cap = cv2.VideoCapture(path)

output_width = 800
output_height = 600

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    #Định nghĩa khoảng màu

    lower_red = np.array([160, 100, 100])
    upper_red = np.array([180, 255, 255])

    lower_green = np.array([40,40,40])
    upper_green = np.array([70,255,255])

    lower_blue = np.array([100,100,100])
    upper_blue = np.array([130,255,255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([20, 255, 255])

    lower_purple = np.array([130, 100, 100])
    upper_purple = np.array([160, 255, 255])

    #Tao mat na cho tung mau 'Mark'

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

    #Tìm viền cho từng màu

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_orange, _ = cv2.findContours(mask_orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_purple, _ = cv2.findContours(mask_purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Vẽ đường viền cho đối tượng

    for cnt in contours_red:
        area = cv2.contourArea(cnt)
        if area > 500:  # Lọc các đối tượng quá nhỏ
            #Lấy vị trí đường viền
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            #Vẽ đường viền và ghi thông tin
            cv2.drawContours(frame, [cnt], 0, (0, 0, 255), 3)
            cv2.putText(frame, f"Red:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    for cnt in contours_green:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 3)
            cv2.putText(frame, f"Green:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    for cnt in contours_blue:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 3)
            cv2.putText(frame, f"Blue:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    for cnt in contours_yellow:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            cv2.drawContours(frame, [cnt], 0, (0, 255, 255), 3)
            cv2.putText(frame, f"Yellow:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    for cnt in contours_orange:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            cv2.drawContours(frame, [cnt], 0, (0, 165, 255), 3)
            cv2.putText(frame, f"Orange:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)

    for cnt in contours_purple:
        area = cv2.contourArea(cnt)
        if area > 500:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]

            #Vẽ viền và in ra màu của object
            cv2.drawContours(frame, [cnt], 0, (255, 0, 255), 3)
            cv2.putText(frame, f"Purple:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)



    resized_frame = cv2.resize(frame, (output_width, output_height))
    cv2.imshow("Candy Crush", resized_frame)

    if cv2.waitKey(100) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()