import plotly.express as px
import tiktok_and_spotify as ts
import pandas as pd
import plotly.graph_objects as go

# fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
# print(fig)
# fig.show()

same_songs_19 = len(ts.intersection_19)
same_songs_20 = len(ts.intersection_20)
same_songs_21 = len(ts.intersection_21)
same_songs_22 = len(ts.intersection_22)

pop_songs_19_amount = len(ts.popsongs_19_set)
pop_songs_20_amount = len(ts.popsongs_20_set)
pop_songs_21_amount = len(ts.popsongs_21_set)
pop_songs_22_amount = len(ts.popsongs_22_set)

tiktok_spotify_19_20 = len(ts.tiktok_to_spotify_19_20)
tiktok_spotify_20_21 = len(ts.tiktok_to_spotify_20_21)
tiktok_spotify_21_22 = len(ts.tiktok_to_spotify_21_22)

spotify_tiktok_19_20 = len(ts.spotify_to_tiktok_19_20)
spotify_tiktok_20_21 = len(ts.spotify_to_tiktok_20_21)
spotify_tiktok_21_22 = len(ts.spotify_to_tiktok_21_22)

new_spotify_tiktok_19_20 = len(ts.new_spotify_19_20)
new_spotify_tiktok_20_21 = len(ts.new_spotify_20_21)
new_spotify_tiktok_21_22 = len(ts.new_spotify_21_22)

new_tiktok_spotify_19_20 = len(ts.new_tiktok_19_20)
new_tiktok_spotify_20_21 = len(ts.new_tiktok_20_21)
new_tiktok_spotify_21_22 = len(ts.new_tiktok_21_22)

# first chart showing amount of same songs appearing in tiktok and spotify charts

df = pd.DataFrame(
    dict(x=['2019', '2020', '2021', '2022'],
         y=[same_songs_19, same_songs_20, same_songs_21, same_songs_22]))
fig = px.line(df, x='x', y='y',
              title='Appearance of TikTok popular songs in spotify charts', text='y', markers=True
              )
fig.update_traces(textposition="top left", textfont_size=14,
                  hovertemplate="<br>".join(["Year: %{x}",
                                             "Number of songs popular in TikTok and Spotify: %{y}"]))

fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Amount of same songs')
fig.add_annotation(x=1, y=95,
                   text="Start of the Covid",
                   yanchor='bottom',
                   showarrow=False,
                   arrowhead=1,
                   arrowsize=1,
                   arrowwidth=2,
                   arrowcolor="#636363",
                   xshift=-80,
                   font=dict(size=20, color="purple", family="Sans Serif")
                   , align="right")
fig.update_layout(shapes=
[
    dict(type='line',
         yref='paper', y0=0, y1=1,
         xref='x', x0=1, x1=1,
         line=dict(color="MediumPurple",
                   width=3,
                   dash="dot")
         )
])
print(fig)
# fig.show()

# comparing influence of spotify and tik tok to each other
spotify_tiktok = pd.DataFrame(
    dict(year=['2019-2020', '2020-2021', '2021-2022'],
         tiktok_to_spotify=[new_tiktok_spotify_19_20, new_tiktok_spotify_20_21, new_tiktok_spotify_21_22],
         spotify_to_tiktok=[new_spotify_tiktok_19_20, new_spotify_tiktok_20_21, new_spotify_tiktok_21_22]
         )
)
year = ['2019-2020', '2020-2021', '2021-2022']
tiktok_to_spotify = [new_tiktok_spotify_19_20, new_tiktok_spotify_20_21, new_tiktok_spotify_21_22]
spotify_to_tiktok = [new_spotify_tiktok_19_20, new_spotify_tiktok_20_21, new_spotify_tiktok_21_22]
# fig_2 = px.line(spotify_tiktok, x='year', y=['tiktok_to_spotify', 'spotify_to_tiktok'],
#                 title='Influence of Spotify top songs and TikTok popular songs to each other', markers=True
#                 )
# fig_2.show()
fig_tsp = go.Figure()
fig_tsp.add_trace(go.Scatter(x=year, y=tiktok_to_spotify, name='TikTok to Spotify', mode='lines+markers',
                             line=dict(color='firebrick', width=2)))
fig_tsp.add_trace(
    go.Scatter(x=year, y=spotify_to_tiktok, name='Spotify to TikTok', mode='lines+markers',
               line=dict(color='royalblue', width=2)))
fig_tsp.update_layout(title='Influence of TikTok popular songs and Spotify top chart songs to each other', xaxis_title='Year', yaxis_title='Number of unique songs that appeared next year',
                      legend=dict(y=0.5, font_size=16))


fig_tsp.show()
