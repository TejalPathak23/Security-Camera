# google search for python openc
# install open cv using --> pip install opencv-python
import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2BGR)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    winsound.Beep(500, 200)
    
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow("Granny Cam", thresh)
