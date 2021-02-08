import json
import datetime
import re
#import matplotlib.pyplot as plt

def normaize_title(str):
    formatted = ''
    for l in str:
        if re.match(r'\w', l):
            print('past if statement')
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
        s = i.get('msPlayed')
        if s > 10000:
            t = i.get('endTime')
            a = i.get('artistName')
            c = i.get('trackName')
            print(c)
            if c in songs:
                print(songs[c])
                songs[c] = songs[c] + 1
            else:
                #format songs for dict
                songs[c] = 1
                # create a sub-dictionary with 

    sh0.close()
    sh1.close()
    # for s in songs:
    #     if s > 5:
           # print(s)


#print_spotify_activity()