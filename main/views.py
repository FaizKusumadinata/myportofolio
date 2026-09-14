from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from main.models import Experience, Artwork, Project
from main.forms import ProjectForm


def show_main(request):
    context = {
        "name": "Faiz Kusumadinata",
        "npm": "2406426196",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia. Born on November 6th, 2006 in the city of Pontianak, West Borneo."
                        "I am interested in art and writing. I also love to spend my time reading novels or drawing."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Faiz Kusumadinata",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_artworks(request):
    context={
        "name": "Faiz Kusumadinata",
        "artworks_list": Artwork.objects.all(),
    }
    return render(request, "artworks.html", context)

def show_art_details(request, id):
    art_detail = get_object_or_404(Artwork, pk=id)
    context = {
        "name": "Faiz Kusumadinata",
        "art_detail":art_detail,
    }
    return render(request, "art_details.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Burhan",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")
    
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")