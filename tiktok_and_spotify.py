import pandas as pd

# spotify_20_21 = pd.read_csv('Spotify_2020-2021_pop_songs.csv')
spotify_20 = pd.read_csv('spotify_top_charts_20.csv')
# spotify_19 = pd.read_excel('Spotify_2019_with_genres.xlsx')
spotify_21 = pd.read_csv('spotify_top_charts_21.csv')
spotify_19 = pd.read_csv('spotify_top_charts_19.csv')
spotify_22 = pd.read_csv('spotify_top_charts_22.csv')
tiktok_19 = pd.read_csv('TikTok_songs_2019.csv')
tiktok_20 = pd.read_csv('TikTok_songs_2020.csv')
tiktok_21 = pd.read_csv('TikTok_songs_2021.csv')
tiktok_22 = pd.read_csv('tiktok_songs_2022.csv')
tiktok_21_new = pd.read_csv('TikTok_songs_2021_otherone.csv')
# pop_songs_19 = spotify_19['Title']
pop_songs_19 = spotify_19['track_name']
pop_songs_20 = spotify_20['track_name']
pop_songs_21 = spotify_21['track_name']
pop_songs_22 = spotify_22['track_name']
# for ind in spotify_20_21.index:
#     year = spotify_20_21['PopYear'][ind]
#     if year == '2020':
#         pop_songs_20.append(spotify_20_21['Title'][ind])
#     elif year == '2021':
#         pop_songs_21.append(spotify_20_21['Title'][ind])
#     else:
#         pop_songs_20.append(spotify_20_21['Title'][ind])
#         pop_songs_21.append(spotify_20_21['Title'][ind])

tiktok_19_names = tiktok_19['track_name']
tiktok_20_names = tiktok_20['track_name']
tiktok_21_names = tiktok_21['track_name']
tiktok_22_names = tiktok_22['track_name']
tiktok_21_names_new = tiktok_21['track_name']

popsongs_19_set = set(pop_songs_19)
tiktok19_set = set(tiktok_19_names)
popsongs_20_set = set(pop_songs_20)
tiktok20_set = set(tiktok_20_names)
popsongs_21_set = set(pop_songs_21)
tiktok21_set = set(tiktok_21_names)
tiktok_21_set_new = set(tiktok_21_names_new)
tiktok_21_more = tiktok21_set.union(tiktok_21_set_new)
tiktok22_set = set(tiktok_22_names)
popsongs_22_set = set(pop_songs_22)
intersection_19 = popsongs_19_set.intersection(tiktok19_set)
intersection_20 = popsongs_20_set.intersection(tiktok20_set)
intersection_21 = popsongs_21_set.intersection(tiktok21_set)
intersection_22 = popsongs_22_set.intersection(tiktok22_set)
intersection_21_new = popsongs_21_set.intersection(tiktok_21_more)
print('Amount of same popular songs in tiktok and spotify at the same year (2019) ', len(intersection_19))
print('Amount of same popular songs in tiktok and spotify at the same year (2020) ', len(intersection_20))
print('Amount of same popular songs in tiktok and spotify at the same year (2021) ', len(intersection_21))
print('Amount of same popular songs in tiktok and spotify at the same year (2021) bigger list ', len(intersection_21_new))
print('Amount of same popular songs in tiktok and spotify at the same year (2022) ', len(intersection_22))


