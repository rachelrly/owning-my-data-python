import json
from datetime import datetime
import re
from spotify_graph import frequent_plays_graph
import random


def normaize_title(str): #replaces spaces and mixed chars with underscores
    formatted = ''
    for l in str:
        if re.match(r'\w', l):
            formatted += l.lower()
        else: 
            formatted += '_'
    return formatted


def get_high_listen_songs(data): 
    #returns a set of titles where listens > 10
    songs = dict()
    for i in data:
        ms_played = i.get('msPlayed')
        if ms_played > 10000: #played for less than a minute
            song_name = i.get('trackName')
            formatted_name = normaize_title(song_name)
            
            if formatted_name not in songs:
                songs[formatted_name] = {"count": 1, "title": song_name}
            else:
                songs[formatted_name]['count'] += 1
               
    high_listen_songs = dict()

    for s in songs:
        if songs[s]['count'] > 110:
            color = "%06x" % random.randint(0, 0xFFFFFF)
            high_listen_songs[s] = {'color' : f'#{color}'}

    return high_listen_songs


def get_individual_listens(high_listen_songs, data): #for high listen songs
    days = list()
    times = list()
    colors = list()
    for i in data:
        title = i.get('trackName')
        formatted_title = normaize_title(title)
        if formatted_title in high_listen_songs: 
            ms_played = i.get('msPlayed')
            if ms_played > 10000:
                colors.append(high_listen_songs[formatted_title]['color'])

                time = i.get('endTime')
                dt = datetime.strptime(time, '%Y-%m-%d %H:%M')

                hour=dt.hour
                minute=dt.minute / 60
                full_time = hour + minute 

                month = dt.month 
                day = dt.day / 31
                part_day = (full_time / 24) / 31
                full_day = month + day + part_day

                days.append(full_day)
                times.append(full_time - 1)

    obj = {'days': days, 'times': times, 'colors': colors}  
    return obj






def print_spotify_activity():
    #open file
    sh1 = open('StreamingHistory1.json', )
    #convert to python
    data = json.load(sh1)

    high_listen_titles = get_high_listen_songs(data) #set of titles
    lists = get_individual_listens(high_listen_titles, data) #gets individual dates for high play songs

    days = lists['days']
    times = lists['times']
    colors = lists['colors']
    
    frequent_plays_graph(days, times, colors) #makes graph

    sh1.close() #close files





print_spotify_activity()
