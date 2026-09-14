from django.urls import path

from main.views import show_main, show_experience, show_artworks, show_art_details, create_project, show_projects, get_projects_json, delete_project

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("artworks/", show_artworks, name="show_artworks"),
    path("art_details/<str:id>/", show_art_details, name="show_art_details"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project")
]