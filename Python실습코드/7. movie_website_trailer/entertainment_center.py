import media
import fresh_tomatoes


# Movie class의 instnace(object) 생성
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=NBepTulmSMw")
# print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=9kJjCdV3JdM")
# print (avatar.storyline)
# avatar.show_trailer()
school_of_rock = media.Movie("School of Rock",
                        "Using rock music to learn",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=oP7kExN8LFA")
ratatouille = media.Movie("Ratatouille",
                        "A Rat is a shef in Paris",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=3YG4h5GbTqU")

midnight_in_paris = media.Movie("Midnight in Paris",
                        "Going back in time to meet authors",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=pbvsAJjxqG4")

hunger_games = media.Movie("Hunger Games",
                        "A really real reality show",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=MXU9eB4gc2Y")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
# open_movies_page 함수 : movies 객체를 input으로 받아 output으로 html file을 생성하고
# html file을 호출하여 web site 보여줌
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
# 아래 __doc__ (""" """을 출력), __name__(class이름 출력), __module__(모듈이름 출력)은 내장된 class 변수임
# ==> (predefined varaibles)
# print (media.Movie.__doc__)
# print (media.Movie.__name__)
# print (media.Movie.__module__)
