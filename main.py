import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, num=100)
y = np.sin(4 * x) * np.exp(-x / 4)
plt.plot(x, y)
plt.show()