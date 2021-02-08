import json
import datetime

def print_spotify_activity():
    #open file
    sh0 = open('StreamingHistory0.json', )
    sh1 = open('StreamingHistory1.json', )
    #convert to python
    data0 = json.load(sh0)
    data1 = json.load(sh1)

    for i in data0:
       # ts = datetime.datetime.fromtimestamp(i['endTime'])
        a = i.get('artistName')
        c = i.get('trackName')
        s = i.get('msPlayed')
        print(f'{a} from {c}, {s}')

    sh0.close()
    sh1.close()


print_spotify_activity()