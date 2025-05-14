class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
   
    def __init__(self, artist, genre ):
        self.artist = artist
        self.genre = genre
        
    #Tracking song count
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    #Add a new genre to the genre list
    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1
        
   
   
