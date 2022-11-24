from . import views
from django.urls import path


app_name = 'signlanguage'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
]
