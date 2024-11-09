import user_generator
import playlist_generator
# import movie_history_generator
import movie_generator
import home_generator

def main():
    user_generator.generate_random_users()
    playlist_generator.generate_movie_collections()
    # movie_history_generator.generate_movie_history()
    movie_generator.generate_movies()
    home_generator.generate_home()

if __name__ == "__main__":
    main()