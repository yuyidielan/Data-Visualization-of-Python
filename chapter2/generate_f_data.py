import string
import random
ROWS=1000000
SAMPLE = '012345678901234567890123456'
F1 = 9
F2 = F1 + 13
F3=F2+4
for i in range(ROWS):
    t=''.join(random.sample(SAMPLE,len(SAMPLE)))
    print(t[0:F1], t[F1:F2], t[F2:F3])