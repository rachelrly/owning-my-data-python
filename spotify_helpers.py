import random
import time
from datetime import datetime
import re


def _normaize_title(str): #replaces spaces and mixed chars with underscores
    formatted = ''
    for l in str:
        if re.match(r'\w', l):
            formatted += l.lower()
        else: 
            formatted += '_'
    return formatted


def _format_date(date_str):
        hour= date_str.hour
        minute=date_str.minute / 60
        full_time = hour + minute 
        #specifically formatted for this data
        month = 0 if date_str.month == 1 else 31
        return full_time
              

def _format_time(date_str): 
    day = date_str.day
    month = date_str.month
    full_day = day if month == 1 else 31+day
    return full_day


def get_high_listen_songs(data): 
    #returns a set of titles where listens > 10
    songs = dict()
    for i in data:
        ms_played = i.get('msPlayed')
        if ms_played > 10000: #played for less than a minute
            song_name = i.get('trackName')
            formatted_name = _normaize_title(song_name)
            
            if formatted_name not in songs:
                songs[formatted_name] = {"count": 1, "title": song_name}
            else:
                songs[formatted_name]['count'] += 1
               
    high_listen_songs = dict()

    for s in songs:
        if songs[s]['count'] > 50:
            color = "%06x" % random.randint(0, 0xFFFFFF)
            high_listen_songs[s] = {'color' : f'#{color}'}

    return high_listen_songs


def get_individual_listens(high_listen_songs, data): #for high listen songs
    days = list()
    times = list()
    colors = list()
        

    for i in data:
        title = i.get('trackName')
        formatted_title = _normaize_title(title)
        if formatted_title in high_listen_songs: 
            ms_played = i.get('msPlayed')
            if ms_played > 10000:
                colors.append(high_listen_songs[formatted_title]['color'])
                time = i.get('endTime')
                dt = datetime.strptime(time, '%Y-%m-%d %H:%M')
                d = _format_date(dt)
                t = _format_time(dt)

                days.append(d)
                times.append(t)

    obj = {'days': days, 'times': times, 'colors': colors}  
    return obj