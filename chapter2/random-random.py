import pylab
import random
SAMPLE_SIZE=100
random.seed()

real_rand_vars=[]

for _ in range(SAMPLE_SIZE):
    new_value=random.random()
    real_rand_vars.append(new_value)
pylab.hist(real_rand_vars,10)

pylab.xlabel("Number range") 
pylab.ylabel("Count") 

# show figure
pylab.show()
