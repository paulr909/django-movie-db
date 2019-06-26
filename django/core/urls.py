from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('movies', views.MovieList.as_view(), name='movie-list'),
    path('movies/top', views.TopMovies.as_view(), name="top-movies"),
    path('movie/<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),
    path('movie/<int:movie_id>/vote', views.CreateVote.as_view(), name='create-vote'),
    path('movie/<int:movie_id>/image/upload', views.MovieImageUpload.as_view(), name='movie-image-upload'),
    path('movie/<int:movie_id>/vote/<int:pk>', views.UpdateVote.as_view(), name='update-vote'),
    path('person/<int:pk>', views.PersonDetail.as_view(), name='person-detail'),
]
