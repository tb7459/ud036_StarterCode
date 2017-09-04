# import here
import fresh_tomatoes
import media

# create variables to hold the links for each picture
# keeping length less than 80 characters.
avatarPic = "https://upload.wikimedia.org/wikipedia/"
avatarPic = avatarPic + "en/b/b0/Avatar-Teaser-Poster.jpg"
promPic = "https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/"
promPic = promPic + "wp-content/uploads/2012/11/prometheusbg3.jpg"
wwPic = "https://cdn.traileraddict.com/content/warner-bros-pictures/"
wwPic = wwPic + "wonder-woman-2017-10.jpg"
dpPic = "https://pre11.deviantart.net/1f9a/th/pre/f/2015/"
dpPic = dpPic + "135/3/3/deadpool_movie_poster_by_chronoxiong-d8tfamw.png"
pbPic = "http://4.bp.blogspot.com/-dT5wdvnKZ1s/Te1XqUzvPHI/AAAAAAAAAPE/"
pbPic = pbPic + "3zluGjAUwlA/s1600/princess-bride.jpg"
wcPic = "http://f.ptcdn.info/049/037/000/"
wcPic = wcPic + "nx8f2tnujPE0mnzOa8U-o.jpg"

# create instances of the Movie object below for avatar,prometheus
# wonder woman, deadpool, princess bride, and warcraft
avatar = media.Movie("Avatar", "A marine on an alien Planet",
                     avatarPic,
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
prom = media.Movie("Prometheus", "Archaeologists find their creators",
                   promPic,
                   "https://www.youtube.com/watch?v=34cEo0VhfGE")
ww = media.Movie("Wonder Woman", "Amazon warrior princess Diana defeats Aries",
                 wwPic,
                 "https://www.youtube.com/watch?v=VSB4wGIdDwo")
dp = media.Movie("Deadpool", "A not-so-super superhero battles his creator",
                 dpPic,
                 "https://www.youtube.com/watch?v=ONHBaC-pfsk")
princess_bride = media.Movie("The Princess Bride", "As you wish...",
                             pbPic,
                             "https://www.youtube.com/watch?v=YU_-MUJRgyQ")
wc = media.Movie("Warcraft", "A pc game comes to the theater",
                 wcPic,
                 "https://www.youtube.com/watch?v=RhFMIRuHAL4")

# create an array of movie instances to send to fresh_tomatoes
movies = [avatar, prom, ww, dp, princess_bride, wc]
fresh_tomatoes.open_movies_page(movies)
