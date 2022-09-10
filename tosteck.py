import cv2 as cv
import random
import os
import matplotlib.pyplot as plt

names = 'edit.png'
n = random.randint(1, 999999)

img = cv.imread("edit57761.png")

grey_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

invert_img = cv.bitwise_not(grey_img)

blur_img = cv.GaussianBlur(invert_img, (111, 111), 0)
#blur_img = cv.GaussianBlur(invert_img, (111, 111), 0)

inverted_blur = 255 - blur_img

def blend(x, y):
    return cv.divide(x, 255 - y, scale=256.0)

final_image = blend(grey_img, blur_img)

if os.path.exists(names) == True:
    n = str(n)
    new_name = 'edit' + str(n)
    cv.imwrite(f'{new_name}.png', final_image)
else:
    cv.imwrite('edit.png', final_image)

cv.imshow('steck image', final_image)
cv.waitKey(0)
cv.destroyAllWindows()

plt.figure(figsize=(14, 12))

plt.subplot(1, 2, 1)
plt.title('Sketch', size=16)
plt.imshow(final_image)
plt.axis('off')
plt.show()
