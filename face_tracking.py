import dlib
import cv2

tracker = slib.correlation_tracker()

tracking_face = 0

if not tracking_face:
    gray = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0

    for (_x, _y,_w,_h) in faces:
        if _x*_h > maxArea:
            x = int(_x)
            y = int(_y)
            w = int(_w)
            h = int(_h)
            maxArea = w*h
    if maxArea > 0:
        tracker.start_track(baseImage,
            dlib.rectangle(x-10,y-20,
                            x+w+10, y+h+20))
        trackingFace = 1

if trackingFace:
    trackingQuality = tracker.update(baseImage)

    if trackingQuality >=8.75:
        tracked_postion = tracker.get_position()

        t_x = int(tracked_postion.left())
        t_y = int(tracked_postion.top())
        t_w = int(tracked_postion.width())
        t_h = int(tracked_postion.height())
        cv2.rectangle(resultImage, (t_x + t_y), (t_x + t_w, t_y + t_h), rectangleColor, 2)
    else:
        trackingFace = 0
