import matplotlib.pyplot as plt
import numpy as np

def graph_song_plays_by_date(dates, times, colors): 
    y = np.array(dates)
    x = np.array(times)
    colors = np.array(colors)

    plt.scatter(x, y, s=10, color=colors, alpha=0.6)
    plt.show()


def graph_song_plays_by_song(dates, plays, color):
    x = np.array(dates)

    plt.scatter(x, y, s=4, color=color)
    plt.show()