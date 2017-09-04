# import webbrowser to open the trailers
import webbrowser


class Video():
    # create class Video, which will be the parent class,
    # with title as a variable.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, video_title):
        self.title = video_title


class Movie(Video):
    # create class Movie, which inherits from Video class
    """ This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # initialize movie variables
        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # open webbrowser and start trailer
        webbrowser.open(self.trailer_youtube_url)
