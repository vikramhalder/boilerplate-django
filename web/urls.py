from django.urls import path
from web.view import views

urlpatterns = [
    path('', views.index, name='index'),
]
