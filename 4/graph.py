#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys

x = []
y = []

count = 0
area = 10  # 0 to 15 point radii

for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    x1,y1 = line.split(' ', 1) # spliting the lines on the basis of tabs
    x.append(float(x1))
    y.append(round(float(y1),3))
    count += 1

colors = [40]*count
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.xlabel("local clustering  coeff-->")
plt.ylabel("TIME TAKEN -->")
plt.show()
print("graph is created, check your current directory for the ploted file")
plt.savefig("matplotlib.png")