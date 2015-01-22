from numpy import *
import matplotlib.pyplot as plt
import time
import numpy as np

def graph():



fig = plt.figure()

ax1 = fig.add_subplot(111)

data = np.genfromtxt('test2.txt', delimiter=',', names=True)

ax1.plot(data['x'], data['y'], color='r', label='the data')
