import datetime
import cv2

cap = cv2.VideoCapture(0)

out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(
    *"XVID"), 20.0, (1920, 1080))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        out.write(frame)
        cv2.imshow("frame", frame)

        # get the frame height and width
        frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # print current date and time
        print("Current date and time: ", datetime.datetime.now())
        print(frame_width)
        print(frame_height)

        out.write(frame)

        # set the frame to gray
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("frame", grey)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
