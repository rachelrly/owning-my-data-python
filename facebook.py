import json
import datetime


def print_facebook_activity:
  #open file
    d = open('account_activity.json', )
  #convert to python
    data = json.load(d)

    for i in data['account_activity']:
        ts = datetime.datetime.fromtimestamp(i['timestamp'])
        a = i.get('action')
        c = i.get('city')
        s = i.get('region')
        print(f'{a} {ts} from {c}, {s}')
    
    d.close()