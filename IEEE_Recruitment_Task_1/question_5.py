import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000) # generates random points sampled from a normal distribution

plt.title("Scatter Plot of a 1000 Points Sampled From a Normal Distribution")

plt.scatter(
    x = [i for i in range(1000)],
    y = data,
    c = "green",
    s = 16,
    linewidth = 0.1,
    marker = "X"
) # create the scatter plot

plt.xlabel("Index")
plt.ylabel("Sampled Value")

plt.grid(linestyle='-', linewidth=.5)

plt.show() # display the plot
