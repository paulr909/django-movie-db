from django.urls import path

from .views import (CreateVote, MovieDetail, MovieImageUpload, MovieList,
                    PersonDetail, TopMovies, TopRatedMovies, UpdateVote)

app_name = "core"

urlpatterns = [
    path("movies", MovieList.as_view(), name="movie_list"),
    path("movies/top", TopMovies.as_view(), name="top_movies"),
    path("movies/rated", TopRatedMovies.as_view(), name="top_rated"),
    path("movie/<int:pk>", MovieDetail.as_view(), name="movie_detail"),
    path("movie/<int:movie_id>/vote", CreateVote.as_view(), name="create_vote"),
    path(
        "movie/<int:movie_id>/image/upload",
        MovieImageUpload.as_view(),
        name="movie_image_upload",
    ),
    path(
        "movie/<int:movie_id>/vote/<int:pk>",
        UpdateVote.as_view(),
        name="update_vote",
    ),
    path("person/<int:pk>", PersonDetail.as_view(), name="person_detail"),
]
