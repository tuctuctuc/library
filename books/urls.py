#создаем вручную
from django.urls import path
from . import views
urlpatterns = [
    path('main/', views.index ) # domainnameORlclhst8000.com/main

]