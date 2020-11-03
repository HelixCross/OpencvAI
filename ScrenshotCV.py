import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
# cv2.namedWindow("ScreenShotCV")

img_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to take picture")
        break
    font = cv2.putText(frame, 'Date & Time: {}'.format(datetime.today()), (7, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                       (0, 0, 255), 2)
    cv2.imshow("ScreenShotCV", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("ESC hit, Closing...")
        break
    elif k % 256 == 32:
        img_name = "OpenCV_Frame_{}.png".format(img_counter)

        cv2.imwrite(img_name, frame)
        print('{} Written!'.format(img_name))
        img_counter += 1
cap.release()
cv2.destroyAllWindows()
