#import webbrowser to open the trailers
import webbrowser

#create class Video, which will be the parent class, with title as
# a variable.
class Video():
  VALID_RATINGS = ["G","PG","PG-13","R"]
  def __init__(self,video_title):
      self.title = video_title


#create class Movie, which inherits from Video class
class Movie(Video):
  """ This class provides a way to store movie related information"""
  #initialize movie variables
  def __init__(self,movie_title, movie_storyline,poster_image,
               trailer_youtube):

      Video.__init__(self,movie_title)
      self.storyline = movie_storyline
      self.poster_image_url = poster_image
      self.trailer_youtube_url = trailer_youtube
      
  #open webbrowser and start trailer
  def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)
