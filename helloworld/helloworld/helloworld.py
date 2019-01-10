
from matplotlib import pyplot as plt
import numpy as np


def helloworld():
    print("Hello World")

def hellochart():
    x = np.random.random(100)
    plt.figure()
    plt.plot(x)
    plt.title("Brownbag 0 Chart")
    plt.show()

