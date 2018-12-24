import re
import numpy as np
import matplotlib.pyplot as plt

fpath = 'input.txt'

contents = open(fpath, 'r').read().splitlines()

lights = np.zeros((356, 4))

for i, line in enumerate(contents):
    lightstr = re.findall('-?\d+',line)
    lights[i] = list(map(int, lightstr))

flag = True


def advance(lights):
    n = 1
    lights[:, 0] += lights[:, 2] * n
    lights[:, 1] += lights[:, 3] * n

n = 10418
lights[:, 0] += lights[:, 2] * n
lights[:, 1] += lights[:, 3] * n

# while flag:
#     advance(lights)
#     plt.scatter(lights[:, 0], lights[:, 1])
#     plt.pause(1)
#     plt.gcf().clear()

plt.scatter(lights[:, 0], lights[:, 1])


plt.show()