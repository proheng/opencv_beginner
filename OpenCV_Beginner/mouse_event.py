import cv2
from numpy import uint8, zeros

events = [i for i in dir(cv2) if "EVENT" in i]  # filter out all the events in cv2

# print(events)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ", ", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        str_xy = str(x) + ", " + str(y)
        cv2.putText(img, str_xy, (x, y), font, .25, (255, 255, 0), 1)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        str_bgr = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, str_bgr, (x, y), font, .25, (0, 255, 255), 1)
        cv2.imshow("image", img)


# img = zeros((512, 512, 3), uint8)
img = cv2.imread("lena.jpg")
# add click_event to the image
cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()