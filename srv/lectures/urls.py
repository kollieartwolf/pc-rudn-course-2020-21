from django.urls import path
from . import views

app_name = 'lectures'

urlpatterns = [
    path('', views.show_list, name='show_list'), 
    path('<slug:lec_slug>/',
         views.show_lecture, 
         name='show_lecture'), 
    ]
