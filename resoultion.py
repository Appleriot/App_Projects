import cv2
import matplotlib.pyplot as plt

img = cv2.imread('color/download (24).png')

sr = cv2.dnn_superres.DnnSuperResImpl_create()

path = 'EDSR_x4.pb'

sr.readModel(path)

sr.setModel('edsr', 4)

result = sr.upsample(img)

resized = cv2.resize(result, dsize=None, fx=4, fy=4)

plt.figure(figsize=(12,8))
plt.imshow(result[:,:,::-1])
plt.imshow(resized[:,:,::-1])
plt.show()

cv2.imwrite('saved.png', result)
