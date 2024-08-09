import cv2
import os
import Color

class ContoursObject:
    def DrawContour(frame,contours,nameColor,color):
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:  # Lọc các đối tượng quá nhỏ
                # Lấy vị trí đường viền
                approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
                x = approx.ravel()[0]
                y = approx.ravel()[1]

                # Vẽ đường viền và ghi thông tin
                cv2.drawContours(frame, [cnt], 0, color, 3)
                cv2.putText(frame, f"{nameColor}:{x}:{y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)