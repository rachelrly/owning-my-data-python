# Owning my Data

Working with the user data from Facebook, Google, and Spotify.

## Codebase

### spotify.py

This file runs a function that parses the json data from `StreamingHistory1.json` and collects the songs that were played more than 10 times over the last two months.

The time information for each of these plays is collected and visualized with Matplotlib in `spotify_graph.py`.

Every dot represents a "play", and each song is randomly assigned a color. 


### facebook.py
