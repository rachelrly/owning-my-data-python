import json
import datetime
import re
#import matplotlib.pyplot as plt

def normaize_title(str): #replaces spaces and mixed chars with underscores
    formatted = ''
    for l in str:
        if re.match(r'\w', l):
            formatted += l.lower()
        else: 
            formatted += '_'
    return formatted


def print_spotify_activity():
    #open file
    sh0 = open('StreamingHistory0.json', )
    sh1 = open('StreamingHistory1.json', )
    #convert to python
    data = json.load(sh0) + json.load(sh1)

    songs = dict()

    for i in data:
       # ts = datetime.datetime.fromtimestamp(i['endTime'])
        ms_played = i.get('msPlayed')
        if ms_played > 10000: #played for less than a minute
            time = i.get('endTime')
            artist_name = i.get('artistName')
            song_name = i.get('trackName')
            formatted_name = normaize_title(song_name)
            
            if formatted_name not in songs:
                songs[formatted_name] = {"count": 1, "artist": artist_name, "title": song_name}
            else:
                print(songs[formatted_name])
                songs[formatted_name]['count'] = songs[formatted_name]['count'] + 1
               

    sh0.close()
    sh1.close()
   # print(songs)


print_spotify_activity()