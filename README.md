# TikTok_impact_on_the_top_charts
In this project, I will examine how TikTok is changing the music industry and how trends songs on TikTok social media influence global top charts. 

I've collected popular songs in TikTok for 2019, 2020, 2021, and 2022 using Spotify API. 
 Spotify does not provide all popular songs from previous years; it also updates weekly top week charts. To get this information, I had to look at other sources.
For this, I performed web scraping using BeautifulSoup on <https://charts.spotify.com/charts/overview/global> . They provide weekly top charts for global 
with next info:
- position of the song in the top chart (from 1 to 200, also showing did the position increased, decreased, or is it re-entry)
- Name of the track and the artist 
- Peak - the highest rank that this entry has ever received in the chart 
- Previous position in the chart
- Streak - the total number of consecutive weeks this entry has been on the chart 
- Streams 

Also, having Track URI using Spotify API, I've collected song features, such as:
- danceability 
- energy 
- key 
- loudness 
- mode 
- speechiness
- acoustics
- instrumentals 
- liveness 
- valence 
- tempo 
- time_signature 
- duration_ms 


Firstly I wanted to look at ***how many popular songs on TikTok appear on Spotify top charts per year***. The result can be seen in the chart below.

<img width="1519" alt="Screenshot 2022-09-02 at 14 33 31" src="https://user-images.githubusercontent.com/46090129/188073925-53e6656c-5b24-4324-a769-5cacb7bee9f3.png">

As we can see through the graphic, the dramatic increase appeared in 2020 - when the Covid started. At that time, many people downloaded the TikTok app and started using it.
The trend is staying the same. 

Secondly, I wanted to look at ***how many songs from one year affect trends on the other platform next year ( Spotify, TikTok)***. Results can be seen on the chart below 
<img width="1546" alt="Screenshot 2022-09-02 at 15 01 18" src="https://user-images.githubusercontent.com/46090129/188078007-6926bb61-7b75-4f43-863f-4dcfc74d6e68.png">

According to these graphics seems like Spotify has more influence on the following year's trends on TikTok than TikTok on the Spotify top charts, especially 
in the 2021-2022 years - only three unique songs from TikTok 2021 trends appeared on 2022 Spotify top charts, while already 60 songs from the 2021 top charts
Spotify songs appeared in 2022 TikTok trend songs. 
