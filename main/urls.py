from django.urls import path

from main.views import show_main, show_experience, show_artworks, show_art_details

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("artworks/", show_artworks, name="show_artworks"),
    path("art_details/<str:id>/", show_art_details, name="show_art_details"),
]