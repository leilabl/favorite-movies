import webbrowser

class Movie():
    """This class provides a structure to organize and display information about movies"""
    valid_ratings = ["G", "PG", "PG-13", "R"]
    #constructor
    def __init__(self, movie_title,movie_storyline,poster_image,trailer_youtube): #'constructor', underscores means it's a special function, 'self' is the new object/instance being creted
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #new method/function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
