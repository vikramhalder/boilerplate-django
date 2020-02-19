from django.urls import path

from api.view import views

urlpatterns = [
    path('', views.index, name='index'),
]
