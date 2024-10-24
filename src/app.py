pip install python-dotenv
pip install spotipy

import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

conection = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id,
                                                              client_secret = client_secret))

electric_callboy_id = "1WNoKxsp715jez1Td4vthc"

response = conection.artist_top_tracks(electric_callboy_id)

if response:
  tracks = response["tracks"]
  names = [tracks[track]['name'] for track in range(len(tracks))]
  duration_mins = [round((tracks[track]['duration_ms']/60000),2) for track in range(len(tracks))]
  popularity = [tracks[track]['popularity'] for track in range(len(tracks))]

data = {'track':names,'duration':duration_mins,'popularity':popularity}

df=pd.DataFrame(data)
print(df)

scatter_plot = sns.scatterplot(data = df, x = "duration", y = "popularity")
fig = scatter_plot.get_figure()

print('We can observe that there is no relation between the duration od a song and its popularity')