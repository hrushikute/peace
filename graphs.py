import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

x=np.arange(10)*50*3.14/50

print x

y=sp.sin(x)
print y

plt.style.use('ggplot')
plt.xlabel('X-axis')
plt.ylabel('Y Axis')


plt.plot(x,y)
plt.show()

