import matplotlib.pyplot as plt
import numpy as np

def frequent_plays_graph(dates, times): 
    x = np.array(dates)
    y = np.array(times)

    plt.scatter(x, y)
    plt.show()