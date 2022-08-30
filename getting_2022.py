### tried with beautful soup - cannot
# import requests
# from bs4 import BeautifulSoup
# import selenium
# from selenium import webdriver
#
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Safari()
# page  = requests.get('https://charts.spotify.com/charts/view/regional-global-weekly/2022-01-13')
# soup = BeautifulSoup(page.content, 'html.parser')
# soup.body.hidden = True
# soup.prettify()
# print(soup)
# # print(list(soup.children))
# # conent = soup.find_all('div', class_="Content-sc-1n5ckz4-0 jyvkLv" )
# # print(conent)
# # print(soup.find_all('tbody'))

## so will do manually

import pandas as pd
from pandas import DataFrame
import glob
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# week_1 = pd.read_csv(
#     '/Users/svetachurina122/PycharmProjects/spotify_data_collection/top_charts_2022/regional-global-weekly-2022-01-13.csv')
# week_2 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-01-20.csv')
# week_3 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-01-27.csv')
# week_4 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-02-03.csv')
# week_5 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-02-10.csv')
# week_6 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-02-17.csv')
# week_7 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-02-24.csv')
# week_8 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-03-03.csv')
# week_9 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-03-10.csv')
# week_10 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-03-17.csv')
# week_11 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-03-24.csv')
# week_12 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-03-31.csv')
# week_13 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-04-07.csv')
# week_14 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-04-14.csv')
# week_15 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-04-21.csv')
# week_16 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-04-28.csv')
# week_17 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-05-05.csv')
# week_18 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-05-12.csv')
# week_19 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-05-19.csv')
# week_20 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-05-26.csv')
# week_21 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-06-02.csv')
# week_22 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-06-09.csv')
# week_23 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-06-16.csv')
# week_24 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-06-23.csv')
# week_25 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-06-30.csv')
# week_26 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-07-07.csv')
# week_27 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-07-14.csv')
# week_28 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-07-21.csv')
# week_29 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-07-28.csv')
# week_30 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-08-04.csv')
# week_31 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-08-11.csv')
# week_32 = pd.read_csv('top_charts_2022/regional-global-weekly-2022-08-18.csv')



files = os.path.join("/Users/svetachurina122/PycharmProjects/spotify_data_collection/top_charts_2021",
                     "regional-global*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df = df.drop(columns=['rank', 'source', 'previous_rank', 'streams'], axis=1)
df = df.drop_duplicates(subset='track_name', ignore_index=True)
print(df)


auth_manager = SpotifyClientCredentials(client_id='88bdee511a5f42759c27f2b9075fa728',
                                        client_secret='6a3b0a7af04e48c4a297a184f5fb7f9d')
sp = spotipy.Spotify(auth_manager=auth_manager)
print(sp.audio_features('0So2sgVa8aJiARPl2P29u2'))
danceability = []
energy = []
key = []
loudness = []
mode = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
time_signature = []
duration_ms = []

for ind in df.index:
    uri = df['uri'][ind]
    audio_features = sp.audio_features(uri)[0]
    danceability.append(audio_features['danceability'])
    energy.append(audio_features['energy'])
    key.append(audio_features['key'])
    loudness.append(audio_features['loudness'])
    mode.append(audio_features['mode'])
    speechiness.append(audio_features['speechiness'])
    acousticness.append(audio_features['acousticness'])
    instrumentalness.append(audio_features['instrumentalness'])
    liveness.append(audio_features['liveness'])
    valence.append(audio_features['valence'])
    tempo.append(audio_features['tempo'])
    time_signature.append(audio_features['time_signature'])
    duration_ms.append(audio_features['duration_ms'])
    # print(features)

df['danceability'] = danceability
df['energy'] = energy
df['key'] = key
df['loudness'] = loudness
df['mode'] = mode
df['speechiness'] =speechiness
df['acousticness'] = acousticness
df['instrumentalness'] = instrumentalness
df['liveness'] =liveness
df['tempo'] = tempo
df['time_signature'] = time_signature
df['duration_ms'] = duration_ms

print(df.head())
df.to_csv('spotify_top_charts_21.csv', index=False)
