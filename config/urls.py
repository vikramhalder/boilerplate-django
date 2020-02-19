from django.contrib import admin
from django.urls import path, include

from web import view
from web.view import views

urlpatterns = [
    path('', views.index_redirect),
    path('u/', include('web.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
