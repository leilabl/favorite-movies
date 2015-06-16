import random
import media
import fresh_tomatoes


interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA") #creates new instance


avatar = media.Movie("Avatar",
                     "A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
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

_2001 = media.Movie("2001: A Space Odyssey",
                    "Humanity finds a mysterious, obviously artificial, object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.",
                    "http://ia.media-imdb.com/images/M/MV5BNDYyMDgxNDQ5Nl5BMl5BanBnXkFtZTcwMjc1ODg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                    "https://www.youtube.com/watch?v=lfF0vxKZRhc")

pulp_fiction = media.Movie("Pulp Fiction",
                "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                "https://www.youtube.com/watch?v=wZBfmBvvotE")

casablanca = media.Movie("Casablanca",
              "Set in unoccupied Africa during the early days of World War II: An American expatriate meets a former lover, with unforeseen complications.",
              "http://ia.media-imdb.com/images/M/MV5BMjQwNDYyNTk2N15BMl5BanBnXkFtZTgwMjQ0OTMyMjE@._V1_SX214_AL_.jpg",
              "https://www.youtube.com/watch?v=EJvlGh_FgcI")

donnie_darko = media.Movie("Donnie Darko",
                "A troubled teenager is plagued by visions of a large bunny rabbit that manipulates him to commit a series of crimes, after narrowly escaping a bizarre accident.",
                "http://ia.media-imdb.com/images/M/MV5BMTczMzE4Nzk3N15BMl5BanBnXkFtZTcwNDg5Mjc4NA@@._V1_SX214_AL_.jpg",
                "https://www.youtube.com/watch?v=ZZyBaFYFySk")

trainspotting = media.Movie("Trainspotting",
                 "Renton, deeply immersed in the Edinburgh drug scene, tries to clean up and get out, despite the allure of the drugs and influence of friends.",
                 "http://ia.media-imdb.com/images/M/MV5BMTg2MzcxNTY3NV5BMl5BanBnXkFtZTgwOTQ5NDQxMDE@._V1_SX214_AL_.jpg",
                 "https://www.youtube.com/watch?v=GmQqhuKmECc")

neverending_story = media.Movie("The NeverEnding Story",
                     "A troubled boy dives into a wonderous fantasy world through the pages of a mysterious book.",
                     "http://ia.media-imdb.com/images/M/MV5BMTI3MDA3NTQ0MF5BMl5BanBnXkFtZTcwNDEwMDMyMQ@@._V1_SY317_CR3,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=UeFni9dOv7c")

movies = [interstellar, avatar, memento, citizen_kane, big_lebowski, matrix, _2001, pulp_fiction, casablanca, donnie_darko, trainspotting, neverending_story]
def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x
#print shuffle(movies)
fresh_tomatoes.open_movies_page(shuffle(movies))
#print media.Movie.valid_ratings[0]
#print media.Movie.__doc__
#print media.Movie.__module__
#print (matrix.storyline)
