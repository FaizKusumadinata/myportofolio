from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
    path("artworks/", api_views.artwork_list, name="artwork-list"),
    path("artworks/<uuid:art_id>/", api_views.art_details, name="artwork-details"),
    path("artworks/<uuid:art_id>/star/", api_views.artwork_star, name="artwork-star"),
]