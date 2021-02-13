import json
from datetime import datetime
import re
from spotify_graph import plays_graph

def normaize_title(str): #replaces spaces and mixed chars with underscores
    formatted = ''
    for l in str:
        if re.match(r'\w', l):
            formatted += l.lower()
        else: 
            formatted += '_'
    return formatted

    # get the name of high count songs
    # loop through data again and filter out with dates




def get_high_listen_songs(data): 
    #returns a set of titles where listens > 10
    songs = dict()
    for i in data:
        ms_played = i.get('msPlayed')
        if ms_played > 10000: #played for less than a minute
            # time = i.get('endTime')
            # dt = datetime.strptime(time, '%Y-%m-%d %H:%M')
            # print(dt)
            # artist_name = i.get('artistName')
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






def print_spotify_activity():
    #open file
    sh0 = open('StreamingHistory0.json', )
    sh1 = open('StreamingHistory1.json', )
    #convert to python
    data = json.load(sh0) + json.load(sh1)

    high_listen_titles = get_high_listen_songs(data) #set of titles

    sh0.close()
    sh1.close()





print_spotify_activity()
#plays_graph()