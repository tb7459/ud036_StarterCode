#import here
import fresh_tomatoes
import media


#create instances of the Movie object below for avatar,prometheus
#wonder woman, deadpool, princess bride, and warcraft

avatar = media.Movie("Avatar", "A marine on an alien Planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


prom = media.Movie("Prometheus","Archaeologists find their creators",
                   "https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/wp-content/uploads/2012/11/prometheusbg3.jpg",
                   "https://www.youtube.com/watch?v=34cEo0VhfGE")

ww = media.Movie("Wonder Woman","Amazonian warrior princess Diana defeats Aries",
                 "https://cdn.traileraddict.com/content/warner-bros-pictures/wonder-woman-2017-10.jpg",
                 "https://www.youtube.com/watch?v=VSB4wGIdDwo")

dp = media.Movie("Deadpool","A not-so-super superhero battles his creator",
                 "https://pre11.deviantart.net/1f9a/th/pre/f/2015/135/3/3/deadpool_movie_poster_by_chronoxiong-d8tfamw.png",
                 "https://www.youtube.com/watch?v=ONHBaC-pfsk")

princess_bride = media.Movie("The Princess Bride","As you wish...",
               "http://4.bp.blogspot.com/-dT5wdvnKZ1s/Te1XqUzvPHI/AAAAAAAAAPE/3zluGjAUwlA/s1600/princess-bride.jpg",
               "https://www.youtube.com/watch?v=GNvy61LOqY0")

wc = media.Movie("Warcraft","A pc game comes to the theater",
                 "http://f.ptcdn.info/049/037/000/nx8f2tnujPE0mnzOa8U-o.jpg",
                 "https://www.youtube.com/watch?v=RhFMIRuHAL4")

#create an array of movie instances to send to fresh_tomatoes 
movies = [avatar,prom,ww,dp,princess_bride,wc]
fresh_tomatoes.open_movies_page(movies)
