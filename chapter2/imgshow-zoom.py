import matplotlib.pyplot as plt
import scipy
import numpy
#load RGB image
bug=scipy.misc.imread('stinkbug.png')
#convert to gray
bug=bug[:,:,0]
#show original image
plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(bug)

#show 'zoomed' region
zbug=bug[100:350,140:350]
plt.subplot(122)
plt.imshow(zbug)

plt.show()