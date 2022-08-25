import pandas as pd

spotify_20_21 = pd.read_csv('Spotify_2020-2021_pop_songs.csv')
spotify_19 = pd.read_excel('Spotify_2019_with_genres.xlsx')
tiktok_19 = pd.read_csv('TikTok_songs_2019.csv')
tiktok_20 = pd.read_csv('TikTok_songs_2020.csv')
tiktok_21 = pd.read_csv('TikTok_songs_2021.csv')
pop_songs_19 = spotify_19['Title']
pop_songs_20 = []
pop_songs_21 = []
for ind in spotify_20_21.index:
    year = spotify_20_21['PopYear'][ind]
    if year == '2020':
        pop_songs_20.append(spotify_20_21['Title'][ind])
    elif year == '2021':
        pop_songs_21.append(spotify_20_21['Title'][ind])
    else:
        pop_songs_20.append(spotify_20_21['Title'][ind])
        pop_songs_21.append(spotify_20_21['Title'][ind])

tiktok_19_names = tiktok_19['track_name']
tiktok_20_names = tiktok_20['track_name']
tiktok_21_names = tiktok_21['track_name']

popsongs_19_set = set(pop_songs_19)
tiktok19_set = set(tiktok_19_names)
popsongs_20_set = set(pop_songs_20)
tiktok20_set = set(tiktok_20_names)
popsongs_21_set = set(pop_songs_21)
tiktok21_set = set(tiktok_21_names)

intersection_19 = popsongs_19_set.intersection(tiktok19_set)
intersection_20 = popsongs_20_set.intersection(tiktok20_set)
intersection_21 = popsongs_21_set.intersection(tiktok21_set)

print(len(intersection_19))
print(len(intersection_20))
print(len(intersection_21))