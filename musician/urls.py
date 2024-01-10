from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.Add_musicianView.as_view(), name='add_musician_url' ),
    path('edit/<int:id>', views.Update_musicianView.as_view(), name='edit_musician'),
]
