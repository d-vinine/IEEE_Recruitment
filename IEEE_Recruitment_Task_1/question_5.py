import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0, 1, 1000) # generates random points sampled from a normal distribution
y = np.random.normal(0, 1, 1000) 

plt.title("Scatter Plot of a 1000 Points Sampled From a Normal Distribution")

plt.scatter(
    x = x,
    y = y,
    c = "green",
    s = 16,
    linewidth = 0.1,
    marker = "X"
) # create the scatter plot

plt.xlabel("X")
plt.ylabel("Y")

plt.grid(linestyle='-', linewidth=.5)

plt.show() # display the plot
