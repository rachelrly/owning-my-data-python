import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import DateFormatter

def graph_song_plays_by_date(dates, times, colors): 
    y = np.array(dates)
    x = np.array(times)
    colors = np.array(colors)

    plt.scatter(x, y, s=20, color=colors, alpha=0.6)
    date_form = DateFormatter('%m-%d')
    plt.get_yaxis().set_major_formatter(date_form)
    plt.show()


def graph_song_plays_with_subplot(dates, times, colors):
    y = np.array(dates)
    x = np.array(times)
    colors = np.array(colors)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x, y)
    # ax.plot(x, y)
    #ax.set_xlim(1, 25)
    ax.set_ylim(dates[0], dates[-1])
    plt.show()


def graph_song_plays_by_song(dates, plays, color):
    x = np.array(dates)

    plt.scatter(x, y, s=4, color=color)
    plt.show()