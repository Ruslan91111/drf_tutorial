from django.contrib import admin
from django.urls import path

from movies.views import MoviesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movieslist', MoviesAPIView.as_view()),
    path('api/v1/movieslist/<int:pk>/', MoviesAPIView.as_view()),


]
