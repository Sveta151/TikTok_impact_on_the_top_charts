import pandas as pd

read_file = pd.read_csv('TikTok_songs_2019.csv')
read_file.to_excel('TikTok_songs_2019.xlsx', index= False)
