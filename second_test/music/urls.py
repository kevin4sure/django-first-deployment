
from django.urls import path,include

from . import views



urlpatterns= [ #name of this list should not be changed
    # /music/
    #path('',views.index,name='music_index'),

    path('',views.IndexView.as_view(),name='music_index'),
    # /music/albums/12/
    #path('albums/<int:album_id>/',views.detail,name='music_detail'),
     path('albums/<pk>/',views.DetailsView.as_view(),name='music_detail'),
    # /music/12/favourite/    #to perform url logic,after selecting the favourite sings, the user will be redirected to the same webpage.
    #path('albums/<int:album_id>/favourite/',views.favourite,name='music_favourite')
    
    # /music/album/add/
    path('album/add/',views.AlbumCreate.as_view(),name='album_add'),
    # /music/album/12/
    path('album/<pk>/',views.AlbumUpdate.as_view(),name='album_update'),
    # /music/12/delete/
    path('albums/<pk>/delete/',views.AlbumDelete.as_view(),name='album_delete'),

    path('register/',views.UserFormView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login')

] 


