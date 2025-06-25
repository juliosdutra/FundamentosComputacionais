import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,20)
y = np.sin(2*np.pi*x)

print(x)
print(y)

plt.figure()
plt.plot(x,y,'o--')
plt.show();
