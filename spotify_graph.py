import matplotlib.pyplot as plt
import numpy as np

def frequent_plays_graph(dates, times, colors): 
    x = np.array(dates)
    y = np.array(times)
    colors = np.array(colors)

    plt.scatter(x, y, s=25, color=colors)
    plt.show()