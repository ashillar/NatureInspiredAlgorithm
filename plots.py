import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Trial1", "Trial2", "Trial3", "Trial4"])
y = np.array([5665964, 5651568, 5661394, 5648236])

plt.bar(x,y)
plt.title('Plot of Experiment 3')
plt.xlabel('Trials')
plt.ylabel('Fitness Values')
plt.show()
plt.savefig('experiment3.png')


x1 = np.array(["Trial1", "Trial2", "Trial3", "Trial4"])
y1 = np.array([5643544, 5629152, 5661394, 5648236])

plt.bar(x1,y1)
plt.title('Plot of Experiment 4 ')
plt.xlabel('Trials')
plt.ylabel('Fitness Values')
plt.show()
plt.savefig('experiment3.png')
