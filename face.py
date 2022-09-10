import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

output_size_width = 775
output_size_height = 600

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2.namedWindow('base-image', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('result-image', cv2.WINDOW_AUTOSIZE)

cv2.moveWindow('base-image',0,100)
cv2.moveWindow('result-image',400, 100)

cv2.startWindowThread()
while True:
    rectangleColor = (0,165,255)

    rc, fullSizeBaseImage = capture.read()

    baseImage = cv2.resize(fullSizeBaseImage, (320,240))

    pressedKey = cv2.waitKey(1)
    if pressedKey == ord('Q'):
        cv2.destroyAllWindows()
        exit(0)

    resultImage = baseImage.copy()

    gray = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0


#Loop over all faces and check if the area for this face is
#the largest so far
    for (_x,_y,_w,_h) in faces:
        if  _w*_h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w*h

    #If one or more faces are found, draw a rectangle around the
    #largest face present in the picture
        if maxArea > 0 :
            cv2.rectangle(resultImage,  (x-10, y-20),
                        (x + w+10 , y + h+20),
                        rectangleColor,2)



#Since we want to show something larger on the screen than the
#original 320x240, we resize the image again
#
#Note that it would also be possible to keep the large version
#of the baseimage and make the result image a copy of this large
#base image and use the scaling factor to draw the rectangle
#at the right coordinates.
    largeResult = cv2.resize(resultImage,
                (output_size_width,output_size_height))


#Finally, we want to show the images on the screen
    cv2.imshow("base-image", baseImage)
    cv2.imshow("result-image", largeResult)
