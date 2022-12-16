from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from movies.views import MoviesAPIList, MoviesAPIUpdate, MoviesAPIDestroy


# класс собстенных созданных маршрутов
# class TryingCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]
# router = routers.DefaultRouter()
# маршрут для custom роутеров
# router.register(r'movies', MoviesViewSet, basename='movies')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')), #аутентификация
    path('api/v1/movies/', MoviesAPIList.as_view()),
    path('api/v1/movies/<int:pk>/', MoviesAPIUpdate.as_view()),
    path('api/v1/moviesdelete/<int:pk>/', MoviesAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # path('api/v1/movieslist', MoviesViewSet.as_view({'get': 'list'})),
    # path('api/v1/movieslist/<int:pk>/', MoviesViewSet.as_view({'put': 'update'})),

    # path('api/v1/moviesdetail/<int:pk>/', MoviesAPIDetailView.as_view()),

]
