import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, exp

x2=[x for x in range(-5,6)]
y2=[y**2 for y in range(-5,6)]

x3=[x for x in range(-5,6)]
y3=[y**3 for y in range(-5,6)]

ex=[x for x in range(-5,6)]
ey=[np.e**y for y in range(-5,6)]

lx=[x for x in range(-5,6)]
ly=[np.log(y) for y in range(-5,6)]

plt.title("График функции y", color='#173554', fontstyle="italic", fontweight="bold")
plt.xlabel('Ось х', color='#173554', fontweight="bold")
plt.ylabel('Ось y', color='#173554', fontweight="bold")
gr = plt.gca()
gr.set_facecolor('#84d8d8')
plt.gcf().set_facecolor('#84d8d8')

plt.plot(x2, y2, color='#173554', marker='o', markersize=7)
plt.plot(x3, y3, color='#773554', marker='x', markersize=7)
plt.plot(ex, ey, color='#d73554', marker='>', markersize=7)
plt.plot(lx, ly, color='#319554', marker='s', markersize=7)
plt.show()
