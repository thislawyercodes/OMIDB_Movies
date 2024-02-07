from django.urls import path

from api.views.movies_views import FetchMoviesApiView

urlpatterns = [
    path('detail',FetchMoviesApiView.as_view(),name='movies_detail'),
]
