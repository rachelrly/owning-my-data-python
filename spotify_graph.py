import matplotlib.pyplot as plt
import numpy as np

def graph_song_plays_by_date(dates, times, colors): 
    x = np.array(dates)
    y = np.array(times)
    colors = np.array(colors)

    plt.scatter(x, y, s=10, color=colors alpha=0.3)
    plt.show()


def graph_song_plays_by_song(dates, plays, color):
    x = np.array(dates)

    plt.scatter(x, y, s=4, color=color)
    plt.show()