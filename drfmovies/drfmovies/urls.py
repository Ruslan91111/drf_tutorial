from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MoviesViewSet


router = routers.SimpleRouter()
router.register(r'movies', MoviesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

    # path('api/v1/movieslist', MoviesViewSet.as_view({'get': 'list'})),
    # path('api/v1/movieslist/<int:pk>/', MoviesViewSet.as_view({'put': 'update'})),

    # path('api/v1/moviesdetail/<int:pk>/', MoviesAPIDetailView.as_view()),

]
