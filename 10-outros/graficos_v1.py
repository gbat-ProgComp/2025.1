import matplotlib.pyplot as plt
import math

plt.plot([0, 50, 90], [20, 30, 250], color="red")
plt.show()

plt.bar([0, 50, 90], [20, 30, 250], color="red")
plt.show()

for angle in range(0, 360):
    plt.plot([angle], [math.sin(angle*3.14/180)], ".", color="red")
    plt.plot([angle], [math.cos(angle*3.14/180)], ".", color="blue")
plt.show()
    
