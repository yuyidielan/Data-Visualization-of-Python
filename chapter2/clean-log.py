from pylab import *
x=1e6*rand(1000)
y=rand(1000)
figure()
subplot(211)
scatter(x,y)
xlim([1e-6,1e6])
subplot(212)
scatter(x,y)
xscale('log')
xlim([1e-6, 1e6])

show()
