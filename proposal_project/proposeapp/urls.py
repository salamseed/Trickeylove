
from django.urls import path

from proposeapp import views

app_name = 'proposeapp'

urlpatterns = [
    path('', views.love, name='love'),
    path('mylove/', views.mylove, name='mylove')

]

