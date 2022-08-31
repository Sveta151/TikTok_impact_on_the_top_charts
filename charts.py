import plotly.express as px
import tiktok_and_spotify as ts
import pandas as pd

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

# first chart

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
fig.show()
