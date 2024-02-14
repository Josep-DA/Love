from django.urls import path
from . import views

urlpatterns = [
    path('', views.love_generator, name="lovegen"),
    path('love/<str:dt>', views.love, name="love"),

]
