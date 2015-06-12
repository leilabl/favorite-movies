import fresh_tomatoes
import media


interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA") #creates new instance


avatar = media.Movie("Avatar",
                     "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#avatar.show_trailer()

memento = media.Movie("Memento",
                      "A man creates a strange system to help him remember things; so he can hunt for the murderer of his wife without his short-term memory loss being an obstacle.",
                      "http://ia.media-imdb.com/images/M/MV5BMTc4MjUxNDAwN15BMl5BanBnXkFtZTcwMDMwNDg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")
#memento.show_trailer()

citizen_kane = media.Movie("Citizen Kane",
                           "Following the death of a publishing tycoon, news reporters scramble to discover the meaning of his final utterance.",
                           "http://ia.media-imdb.com/images/M/MV5BMTQ2Mjc1MDQwMl5BMl5BanBnXkFtZTcwNzUyOTUyMg@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                           "https://www.youtube.com/watch?v=zyv19bg0scg")


big_lebowski = media.Movie("The Big Lebowski",
                           '"The Dude" Lebowski, mistaken for a millionaire Lebowski, seeks restitution for his ruined rug and enlists his bowling buddies to help get it.',
                           "http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y")


matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

movies = [interstellar, avatar, memento, citizen_kane, big_lebowski, matrix]
fresh_tomatoes.open_movies_page(movies)
#print media.Movie.valid_ratings[0]
#print media.Movie.__doc__
#print media.Movie.__module__
