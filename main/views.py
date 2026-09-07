from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from main.models import Experience


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