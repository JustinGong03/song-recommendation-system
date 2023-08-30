import streamlit as st 
import pandas as pd
import numpy as np
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '87b954ab1feb456d860986363851e7b0'
client_secret = 'ead8e4be77ef4de583cd8474c95c0ab8'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#attempts to retrieve playlist songs from playlist link, otherwise prompts an error message
def process_link(playlist_link): 
    try: 
        playlist_uri = playlist_link.split("?")[0][34:]
        output = sp.playlist(playlist_uri)
        return output
    except: 
        return None

def display_playlist_tracks(playlist_info):
    songs_html = f"""
    <div style="height: 300px; overflow-y: scroll; border: 1px solid #ccc; padding: 20px;">
        <h2 style="color: #FFFFFF; font-size: 1.5em; margin-bottom: 10px;">Playlist name: {playlist_info['name']}</h2>"""
    
    playlist_tracks = playlist_info['tracks']['items']
    
    for track in playlist_tracks:
        song_artists = ', '.join([x['name'] for x in track['track']['artists']])
        song_html = f"""
        <div class="song-item">
            <img src="{track['track']['album']['images'][0]['url']}" alt="Song Cover" class="song-cover">
            <div class="song-info">
                <h3 class="song-title">{track['track']['name']}</h3>
                <p class="song-artist(s)">{song_artists}</p>
            </div>
        </div>"""
        songs_html += song_html
    
    songs_html += """</div>
        <style>
            .song-item {
                display: flex;
                align-items: center;
                gap: 10px;
                padding: 10px;
                border-bottom: 1px solid #ccc;
            }
            .song-cover {
                width: 60px;
                height: 60px;
                object-fit: cover;
            }
            .song-info {
                flex-grow: 1;
            }
            .song-title {
                font-size: 1.2em;
                margin: 0;
            }
            .song-artist {
                font-size: 0.9em;
                margin: 0;
                color: #888;
            }
        </style>
    """
    st.markdown(songs_html, unsafe_allow_html=True)
    
def display_playlist_tracks_results(playlist_info):
    songs_html = f"""
    <div style="height: 300px; overflow-y: scroll; border: 1px solid #1DB954; padding: 20px;">
        <h2 style="color: #FFFFFF; font-size: 1.5em; margin-bottom: 10px;">Song Recommendations</h2>"""
    
    playlist_tracks = playlist_info['tracks']['items']
    
    for track in playlist_tracks:
        song_artists = ', '.join([x['name'] for x in track['track']['artists']])
        song_html = f"""
        <div class="song-item">
            <img src="{track['track']['album']['images'][0]['url']}" alt="Song Cover" class="song-cover">
            <div class="song-info">
                <h3 class="song-title">{track['track']['name']}</h3>
                <p class="song-artist(s)">{song_artists}</p>
                <audio controls style="width: 100%;">
                    <source src="{track['track']['preview_url']}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
        </div>"""
        songs_html += song_html
    
    songs_html += """</div>
        <style>
            .song-item {
                display: flex;
                align-items: center;
                gap: 10px;
                padding: 10px;
                border-bottom: 1px solid #ccc;
            }
            .song-cover {
                width: 60px;
                height: 60px;
                object-fit: cover;
            }
            .song-info {
                flex-grow: 1;
                display: flex;
                flex-direction: column;
            }
            .song-title {
                font-size: 1.2em;
                margin: 0;
            }
            .song-artist {
                font-size: 0.9em;
                margin: 0;
                color: #888;
            }
        </style>
    """
    st.markdown(songs_html, unsafe_allow_html=True)

def find_song_recommendations(playlist_info): 
    print("hello world")
    
def main(): 
    title_style = """<style>
                    .title {
                        font-size: 30px;
                        font-family: 'verdana', sans-serif;
                        font-weight: bold;
                        color: #1DB954;
                 }
                 </style>"""
    
    st.markdown(title_style, unsafe_allow_html=True)
    st.markdown("<p class='title'>Justin's Song Recommendation System</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3) 

    with col1:
        st.write("") 

    with col2: 
        st.image('spotify-logo.png', caption = "Spotify Logo", width = 150)

    with col3:
        st.write("") 
    
    instructions_style = """
    <div style="background-color: #1DB954; padding: 10px; border-radius: 5px; margin-bottom: 20px; text-align: left;">
            <h4>Welcome!</h4>
            Simply enter a spotify playlist link (public or private) below and see the songs that you can add to enhance your playlist!
            <br>
            <br>
            In order to get the best performance, please use a playlist with a particular theme and/or genre. To get best search time, use playlists that have less than 50 songs.
        </div>
    """
    
    st.markdown(instructions_style, unsafe_allow_html=True)
    
    user_playlist = st.text_input("Enter your full spotify playlist link:")  
    # 
    if st.button("Submit"):
        playlist_info = process_link(user_playlist)
        if playlist_info is None:
            st.error("Invalid playlist link. Please enter again.")
        else: 
            st.success("Playlist retrieved!")
            st.write("Your playlist: ")
            display_playlist_tracks(playlist_info)
            st.write("")
            with st.spinner("Retrieving song recommendations..."):
                time.sleep(5)
                playlist_results = process_link("https://open.spotify.com/playlist/2f9LoZiJ2H2UQSUC8y2W2X?si=cb6f77ffbcfa4de1")
            st.write("Your recommended songs:")
            display_playlist_tracks_results(playlist_results)
            
            
                
if __name__ == "__main__":
    main() 
    




