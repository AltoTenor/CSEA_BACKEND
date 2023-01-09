# CSEA_BACKEND
A backend made using python and flask for creating a songs and playlist API. The api is hosted in http://altotenor2002.pythonanywhere.com.
For now the backend supports the following features-
- GET /songs
returns all the songs present in the database in a jsonify-d format
- POST /songs
allows a person to add information about a new song in the database essentially creating a row with 3 paramters (title, album, artist).
(This feature can be checked by putting raw json information in the body tab of the website through Postman.) 
- GET /songs/<id>
returns a specific song and its information by id provided
- DELETE /songs/id \n
deletes the specific song by id from the database
- DELETE /delete_all_songs (additional)
deletes all the songs from the database
- GET /playlists
returns all the playlists which are currently present in the playlists database.

While the "playlists" database was made, due to lack of time and knowledge on my part, all the api calls related to playlists could not be completed.
The databases are made in such a way that a 1 song is already pre inserted- {"Perfect","Ed Sheeran","21"} and 2 playlists are also inserted {"Darker Faces",4} and {"Face my Fears",5}.
