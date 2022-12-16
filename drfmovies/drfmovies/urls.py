from django.contrib import admin
from django.urls import path

from movies.views import MoviesAPIList, MoviesAPIUpdate, MoviesAPIDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movieslist', MoviesAPIList.as_view()),
    path('api/v1/movieslist/<int:pk>/', MoviesAPIUpdate.as_view()),
    path('api/v1/moviesdetail/<int:pk>/', MoviesAPIDetailView.as_view()),

]
