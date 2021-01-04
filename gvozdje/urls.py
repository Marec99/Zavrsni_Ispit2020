from django.urls import path

from . import views

urlpatterns = [
    path('user', views.user, name='userPage'),
    path('mreza', views.mreza, name='mrezaPage'),
    path('', views.gvozdje, name='gvozdjePage'),
]