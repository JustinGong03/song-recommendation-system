# Song Recommendation System: kNN-Based Playlist Enhancer 
## Author: Justin Gong

This project is a user-based data science project which leverages API fetching, classical machine learning techniques, and experimental feedback to recommend songs using Spotify playlists. Below is a demonstration of how the application works: 

https://github.com/JustinGong03/song-recommendation-system/assets/92960950/24f55a94-fd8e-4b36-8235-5cddc0db0223

## Breakdown of Project Contents

**data**: Contains the spotify audio features data and user survey results 

**notebooks**:
- **main_notebook.ipynb**: Centralized notebook with the product development process including the modeling, data analysis, and API fetching.
- **user_survey_results.ipynb**: An in-depth analysis of the pre-user survey and the post-user feedback survey
- **abtesting.ipynb**: An overview of the experimental design to determine the kNN-based model to choose based on user-tested survey

**song_recommendation_system_streamlit.py**: Python script in creating the user-interactive application for the final recommendation system 

**project_demo.mp4**: The mp4 file attached above

## Dataset and Spotipy API

This project relied on the following dataset from kaggle: https://www.kaggle.com/datasets/tomigelo/spotify-audio-features 

It also drew from the Spotipy API to extract and retrieve information on playlists. Through this API, I was able to search inputted playlists through a link, and retrieve crucial information regarding the songs, including artists, audio features, genre, cover album, and more. For more documentation on the spotipy API, please visit the following: https://spotipy.readthedocs.io 

## User Testing and Experimental Design 

This project focuses heavily on user testing to develop a user-based recommendation system. Due to a lack of publicably available spotify data, I was not able to create a "traditional" recommendation system using collaborative filtering to perform social network analysis and pull songs from similar users. Therefore, I needed a recommendation method solely based on the provided songs. Due to ambiguity as to how this should be done, it required user surveying to gather information on what are the most significant features for song recommendations in a playlist. In doing so, I produced three surveys, all linked below: 

**Pre-User Survey**: https://forms.gle/MU8qBfeUjDZtiWjL7

This survey was performed prior to starting the project. This gathered information on what are the most important features of recommended songs to my audience. 

**Model Testing Survey**: https://forms.gle/seuH4Z1WRARt7sZb7

This survey was done during the model construction process. In creating the kNN model, I had two algorithms in generating song recommendations. This survey was part of a blind experiment for users to evaluate the accuracy of each model. 

**User-Feedback Survey**: https://forms.gle/QcMXaZBT4gqCi2BB9

This survey was done at the end of the project to gather user feedback and to evaluate the overall performance of my final model. 

For a more in-depth description of the experimental designs, analysis of results, and conclusions, please see *abtesting.ipynb* and *user_testing_results.ipynb*. 

## Recommendation System Model 

The following methology was used for the final model: 

- 80% of base score calculated from the euclidean distance of the audio features, found through e^(-1*x) where x represents the distance.
- 20% of base score calculated by the popularity of the song (provided by API)

- Potentially up to 0.25 additional points with the amount of points proportional to the presence of the song's **genre** in the playlist 
- Potentially up to 0.20 additional points with the amount of points proportional to the prescence of the song's **artists** in the playlist
- An additional 0.1 provided to songs that were also recommended by the Spotipy API

NOTE: Songs that exceeded a 1.00 recommendation score were capped at 1.00. 

These numbers and methology was significantly influenced through the user testing mentioned previously. The numbers and contributions of different categories were assigned according to user preferences. Please refer to those respective notebooks for a more in-depth analysis of the conclusions. 

## Final Takeaways 

In the end, the current recommendation system performs very well with high user satisfaction rates. However, it is important to consider the following drawbacks and improvements derived from the user feedback. 

1. Run time

Currently, the run time is incredibly slow. Playlists that are ~50 songs long will have an expected run time of approximately 40-45 seconds. This is primarily due to the API calls that are being made, as the song information is not being retrieved locally. This communication with Spotipy requires a large wait time. A potential improvement in the future is storaging songs into a SQL database to make searches be performed locally. 

2. Broader scope on playlist requirements

The final model relies heavily on a playlist having an overaching "theme" to it. For example, in my demonstration, I selected a party playlist with upbeat songs. Through this, the model can find songs that fit the theme similarly. This is because the model is primarily fetching songs through finding similar audio features to the "average" song in the playlist. A way this can be improved is by considering the distances of each song to the "average" audio features by looking at the standard deviations, and adjust the model metrics accordingly. 

3. Increase song bank capacity

The current model utilizes a kaggle dataset with 130k songs with some additional songs from the Spotipy API. This is not nearly enough data to pull from considering there are millions of songs on spotify alone. This means the scope of songs that can be selected from is incredibly small. A way this can be improved is similar to the solution in point 1.), where I have a local SQL database to hold spotify songs. However, this will require local storage capacity and a long pre-loading time. 

5. Expand from spotify playlists

The current recommendation system is achieved by taking a spotify playlist as an input. A way this product can be expanded is by accepting other playlists as well, such as Apple Music and YouTube Music. However, this requires additional research on APIs to retrieve song information on these platforms. 
