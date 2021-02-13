import json
from datetime import datetime
import re
from spotify_graph import frequent_plays_graph


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
               
    high_listen_songs = set()

    for s in songs:
        if songs[s]['count'] > 10:
            high_listen_songs.add(songs[s]['title'])

    return high_listen_songs


def get_individual_listens(high_listen_songs, data): #for high listen songs
    days = list()
    times = list()
    for i in data:
        title = i.get('trackName')
        if title in high_listen_songs: 
            ms_played = i.get('msPlayed')
            if ms_played > 10000:
                time = i.get('endTime')
                dt = datetime.strptime(time, '%Y-%m-%d %H:%M')

                month = dt.month
                day = dt.day
                day_decimal = day / 31
                full_day = month + day_decimal
                days.append(full_day)

                hour=dt.hour
                minute=dt.minute
                minute_decimal = minute / 60
                full_time = hour + minute_decimal
                times.append(full_time)

               # print(f'title: {title} date: {full_day} time: {full_time}')
    obj = {'days': days, 'times': times}  
    return obj






def print_spotify_activity():
    #open file
    sh0 = open('StreamingHistory0.json', )
    sh1 = open('StreamingHistory1.json', )
    #convert to python
    data = json.load(sh0) + json.load(sh1)

    high_listen_titles = get_high_listen_songs(data) #set of titles
    lists = get_individual_listens(high_listen_titles, data) #gets individual dates for high play songs

    days = lists['days']
    times = lists['times']

    frequent_plays_graph(days, times)

    sh0.close() #close files
    sh1.close()





print_spotify_activity()
