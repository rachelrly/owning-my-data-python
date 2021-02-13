import json
from spotify_graph import graph_song_plays_by_date
from spotify_helpers import get_high_listen_songs
from spotify_helpers import get_individual_listens

def generate_spotify_activity():
    #open file
    sh1 = open('StreamingHistory1.json', )
    #convert to python dict
    data = json.load(sh1)

    sh1.close() #close files

    return data



def handle_spotify_activity():
    data = generate_spotify_activity()

    high_listen_titles = get_high_listen_songs(data) #set of titles
    lists = get_individual_listens(high_listen_titles, data) #gets individual dates for high play songs

    days = lists['days']
    times = lists['times']
    colors = lists['colors']
    
    graph_song_plays_by_date(days, times, colors) #makes graph


handle_spotify_activity()