import cv2
import numpy as np
import imutils

# Set ranges of yellow color
lower_low_yellow = np.array([28, 70, 90])
upper_low_yellow = np.array([32, 255, 255])
lower_high_yellow = np.array([19, 118, 119])
upper_high_yellow = np.array([27, 255, 255])

# Set ranges of blue color
lower_low_blue = np.array([91, 38, 172])
upper_low_blue = np.array([102, 255, 255])
lower_high_blue = np.array([99, 110, 142])
upper_high_blue = np.array([105, 255, 255])
lower_deep_blue = np.array([113, 125, 142])
upper_deep_blue = np.array([123, 255, 255])

# Set ranges of red color
lower_red = np.array([170, 106, 120])
upper_red = np.array([179, 255, 255])
lower_green = np.array([34, 130, 10])
upper_green = np.array([77, 255, 255])

# Set ranges of mango color
lower_low_mango = np.array([137, 100, 100])
upper_low_mango = np.array([155, 255, 255])
lower_deep_mango = np.array([157, 120, 120])
upper_deep_mango = np.array([163, 255, 255])

# Set ranges of orange color
lower_low_orange = np.array([10, 100, 90])
upper_low_orange = np.array([20, 255, 255])
lower_deep_orange = np.array([0, 118, 97])
upper_deep_orange = np.array([8, 255, 255])

# Code to set frame size of video display
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 580)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

while True:
    _, video = cap.read()
    convert_color = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # set mask for low yellow
    mask_low_yellow = cv2.inRange(convert_color, lower_low_yellow, upper_low_yellow)
    contours_low_yellow, hierarchy = cv2.findContours(mask_low_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_low_yellow) != 0:
        for contour in contours_low_yellow:
            if cv2.contourArea(contour) > 200:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x+w, y+h), (25, 250, 255), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Yellow > 50%", (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (30, 255, 255), 2)

    # set mask for high yellow
    mask_high_yellow = cv2.inRange(convert_color, lower_high_yellow, upper_high_yellow)
    contours_high_yellow, hierarchy = cv2.findContours(mask_high_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_high_yellow) != 0:
        for contour in contours_high_yellow:
            if cv2.contourArea(contour) > 200:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (25, 250, 255), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Yellow 80% - 90%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (30, 255, 255), 2)

    # set mask for red color       
    mask_red = cv2.inRange(convert_color, lower_red, upper_red)
    contours_red, hierarchy = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_red) != 0:
        for contour in contours_red:
            if cv2.contourArea(contour) > 200:
                
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x+w, y+h), (0, 0, 255), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Red > 90%", (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # set mask for green color
    mask_green = cv2.inRange(convert_color, lower_green, upper_green)
    contours_green, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_green) != 0:
        for contour in contours_green:
            if cv2.contourArea(contour) > 200:
                
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x+w, y+h), (45, 190, 10), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Green >90%", (x-5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (45, 190, 10), 2)

    # set mask for blue color
    mask_low_blue = cv2.inRange(convert_color, lower_low_blue, upper_low_blue)
    contours_low_blue, hierarchy = cv2.findContours(mask_low_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_low_blue) != 0:
        for contour in contours_low_blue:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (231, 100, 92), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Blue > 60%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (231, 100, 92), 2)

    # set mask for blue color
    mask_high_blue = cv2.inRange(convert_color, lower_high_blue, upper_high_blue)
    contours_high_blue, hierarchy = cv2.findContours(mask_high_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_high_blue) != 0:
        for contour in contours_high_blue:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (205, 93, 82), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Blue > 80%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (205, 93, 82), 2)

    # set mask for blue color
    mask_deep_blue = cv2.inRange(convert_color, lower_deep_blue, upper_deep_blue)
    contours_deep_blue, hierarchy = cv2.findContours(mask_deep_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_deep_blue) != 0:
        for contour in contours_deep_blue:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (196, 63, 77), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Deep Blue > 95%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (196, 63, 77), 2)

    # set mask for mango color
    mask_low_mango = cv2.inRange(convert_color, lower_low_mango, upper_low_mango)
    contours_low_mango, hierarchy = cv2.findContours(mask_low_mango, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_low_mango) != 0:
        for contour in contours_low_mango:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (300, 29, 100), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Mango > 70%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (300, 29, 100), 2)

    mask_deep_mango = cv2.inRange(convert_color, lower_deep_mango, upper_deep_mango)
    contours_deep_mango, hierarchy = cv2.findContours(mask_deep_mango, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_low_mango) != 0:
        for contour in contours_deep_mango:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (300, 29, 100), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Deep Mango > 95%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (300, 29, 100), 2)

    # set mask for orange color
    mask_low_orange = cv2.inRange(convert_color, lower_low_orange, upper_low_orange)
    contours_low_orange, hierarchy = cv2.findContours(mask_low_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_low_orange) != 0:
        for contour in contours_low_orange:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (23, 57, 82), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Orange > 70%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (23, 57, 82), 2)

    mask_deep_orange = cv2.inRange(convert_color, lower_deep_orange, upper_deep_orange)
    contours_deep_orange, hierarchy = cv2.findContours(mask_deep_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours_low_mango) != 0:
        for contour in contours_deep_orange:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0,150, 152), 2)
                M = cv2.moments(contour)
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(video, (cx, cy), 3, (255, 255, 255), -1)
                cv2.putText(video, "Deep Orange > 95%", (x - 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 207, 202), 2)

    cv2.imshow("mask", mask_deep_blue)
    cv2.imshow("frame", video)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()