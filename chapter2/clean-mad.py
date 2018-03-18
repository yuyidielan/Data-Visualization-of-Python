import numpy as np
import matplotlib.pyplot as plt
def is_outliner(points,threshold=3.5):
    if len(points.shape)==1:
        points=points[:,None]
    median=np.median(points,axis=0)
    diff=np.sum((points-median)**2,axis=-1)
    diff=np.sqrt(diff)
    med_abs_deviation=np.median(diff)
    modified_z_score = 0.6745 * diff / med_abs_deviation
    return modified_z_score > threshold
x=np.random.random(100)
buckets=50
x = np.r_[x, -49, 95, 100, -100]
filtered = x[~is_outliner(x)]

plt.figure()

plt.subplot(211)
plt.hist(x, buckets)
plt.xlabel('Raw')

plt.subplot(212)
plt.hist(filtered, buckets)
plt.xlabel('Cleaned')

plt.show()

