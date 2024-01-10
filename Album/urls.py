from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_album/', views.AlbumView.as_view(), name='add_album' ),
    path('update_album/<int:id>', views.UpdateAlbum.as_view(), name='update_album' ),
    path('deleteAlbum/<int:id>', views.DeleteAlbum.as_view(), name='DeleteAlbum' ),
]
