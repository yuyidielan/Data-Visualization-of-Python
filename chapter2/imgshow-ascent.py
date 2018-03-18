import scipy.misc
import matplotlib.pyplot as plt
ascent= scipy.misc.ascent()
plt.gray()
plt.imshow(ascent)
plt.colorbar()
plt.show()
