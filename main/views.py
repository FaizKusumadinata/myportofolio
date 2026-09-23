import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from main.models import Experience, Artwork, Project
from main.forms import ProjectForm, ArtworkForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Faiz Kusumadinata",
        "npm": "2406426196",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia. Born on November 6th, 2006 in the city of Pontianak, West Borneo."
                        "I am interested in art and writing. I also love to spend my time reading novels or drawing."
        ),
        "last_login":last_login
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Faiz Kusumadinata",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_artworks(request):
    json_response = get_artworks_json(request)
    
    artworks = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    artworks = [artwork.object for artwork in artworks]
    tags_query = request.GET.get("tags", "").strip()

    context = {
        "name": "Faiz Kusumadinata",
        "artworks_list": artworks,
        "tags_query": tags_query,
    }
    return render(request, "artworks.html", context)

def show_art_details(request, id):
    art_detail = get_object_or_404(Artwork, pk=id)
    context = {
        "name": "Faiz Kusumadinata",
        "art_detail":art_detail,
    }
    return render(request, "art_details.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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
        json_response.content.decode("utf-8"),
        "json", projects, use_natural_foreign_keys=True   
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

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def delete_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == "POST":
        artwork.delete()
        messages.success(request, "Artwork Successfully Deleted")
        return redirect("main:show_artworks")

    return redirect("main:show_artworks")

@login_required(login_url="/login/")
def create_artwork(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ArtworkForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Artwork Has Been Submitted")
        return redirect("main:show_artworks")

    context = {
        "name": "Faiz Kusumadinata",
        "form": form,
    }
    return render(request, "artwork_form.html", context)

def get_artworks_json(request):
    title_query = request.GET.get("title", "").strip()
    artworks = Artwork.objects.all()

    if title_query:
        artworks = artworks.filter(title__icontains=title_query)

    artworks_json = serializers.serialize("json", artworks)
    return HttpResponse(artworks_json, content_type="application/json")

@login_required(login_url="/login/")
def update_artwork(request, artwork_id):
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    form = ArtworkForm(request.POST or None, instance=artwork)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_artworks')
    context = {
        'form': form
    }

    return render(request, "artwork_update.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

