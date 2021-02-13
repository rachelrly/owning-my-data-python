import matplotlib.pyplot as plt
import numpy as np

def frequent_plays_graph(dates, times, colors=None): 
    x = np.array(dates)
    y = np.array(times)
    # colors = np.array(colors)

    plt.scatter(x, y, s=4)
    plt.show()