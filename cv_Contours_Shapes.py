import cv2
import numpy as np

def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area > 500:
            cv2.drawContours(imcont, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objcorn = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objcorn == 3: objectType = "Triangle"
            elif objcorn == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objcorn > 4: objectType = "Circle"
            else: objectType = "None"

            cv2.rectangle(imcont, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imcont, objectType, (x + (w//2) - 10, y + (h//2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                        (0, 0, 0), 2)



img = cv2.imread("/Users/Hetze/OneDrive/Desktop/22.jpg")
imcont = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
imgcanny = cv2.Canny(blur, 50, 50)
getcontours(imgcanny)
imgblank = np.zeros_like(img)


cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Image", img)
cv2.imshow("Contour", imcont)
cv2.waitKey(0)
