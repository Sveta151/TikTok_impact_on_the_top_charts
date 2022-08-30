import pandas as pd

data = pd.read_csv('Spotify_2020-2021_genres_and_country.csv')
result = data.dtypes
years = []
data.drop('Unnamed: 0.1', inplace=True, axis=1)
data.drop('Unnamed: 0', inplace=True, axis=1)
print(data.columns)
for ind in data.index:
    our_string = data['HighestChartingWeek'][ind]
    our_string = our_string.split('-')
    if our_string[0] == our_string[4]:
        years.append(our_string[0])
    else:
        years.append([our_string[0], our_string[4]])
data['PopYear'] = years

data.to_csv('Spotify_2020-2021_pop_songs.csv', index=False)
