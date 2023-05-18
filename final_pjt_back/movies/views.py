from .models import Genre, Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, MovieSerailizer
from rest_framework import status
import requests
from django.http import JsonResponse

# id = movie_pk 에 해당하는 영화의 세부사항을 반환한다.
@api_view(['GET'])
def movie_detail(request, movie_pk):

    movie = Movie.objects.get(pk = movie_pk)
    serializer = MovieSerailizer(movie)
    return Response(serializer.data)

# search_str 을 포함하는 제목을 가진 영화들을 반환한다.
@api_view(['GET'])
def search_movie(request, search_str):
    movies_title = Movie.objects.filter(title__contains = search_str)
    movies_original_title = Movie.objects.filter(original_title__contains = search_str)
    movies = movies_title.union(movies_original_title)
    movie_lst = []

    for movie in movies:
        movie_lst.append(MovieSerailizer(movie).data)

    return JsonResponse(movie_lst, safe=False)

# db에 영화 정보를 채운다.
@api_view(['GET'])
def make_movies(request):

    for id in range(100, 1000):
        response = requests.get(f"https://api.themoviedb.org/3/movie/{id}?language=ko-KR&api_key=f71b3408ea6ab0e8ac8a36b985605a43")
        json_movie = response.json()

        if 'success' in json_movie:
            continue

        movie = Movie.objects.create(
            id = json_movie['id'],
            title = json_movie['title'],
            adult = json_movie['adult'],
            original_language = json_movie['original_language'], 
            original_title = json_movie['original_title'],
            overview = json_movie['overview'],
            popularity = json_movie['popularity'],
            poster_path = json_movie['poster_path'],
            release_date = json_movie['release_date'],
            runtime = json_movie['runtime'],
            vote_average = json_movie['vote_average'],
        )

        for genre_info in json_movie['genres']:
            genre = Genre.objects.get(id = genre_info['id'])
            movie.genres.add(genre)

    return Response("good")

# db에 장르 정보를 채운다.
@api_view(['GET'])
def make_genres(request):

    response = requests.get('https://api.themoviedb.org/3/genre/movie/list?language=ko-KR&api_key=f71b3408ea6ab0e8ac8a36b985605a43')
    genres = response.json()
    for genre_info in genres['genres']:
        Genre.objects.create(
            id = genre_info['id'],
            name = genre_info['name']
        )

    return Response("good")
