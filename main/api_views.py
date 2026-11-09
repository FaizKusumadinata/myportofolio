from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Project, Artwork
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ProjectSerializer, ArtworkSerializer

#Project Views

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_list(request):
    if request.method in ("GET", "HEAD"):
        projects = Project.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            projects = projects.filter(title__icontains=title)
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = ProjectSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_detail(request, project_id):
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"), pk=project_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ProjectSerializer(
        project, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

#Artwork Views

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def artwork_list(request):
    if request.method == ("GET", "HEAD"):
        artwork = Artwork.objects.all()#prefetch_related("starred_by").order_by("title", "id")
        art_title = request.query_params.get("title", "").strip()
        if art_title:
            artwork = artwork.objects.all() #filter(title__icontains=art_title)
        serializer = ArtworkSerializer(Artwork, many=True)#, context={"request":request})
        return Response(serializer.data)
    
    serializer = ArtworkSerializer(data=request.data, context={"request":request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def art_details(request, art_id):
    artwork = get_object_or_404(Artwork.objects.prefetch_related("starred_by"), pk=art_id)
    if request.method in ("GET", "HEAD"):
        serializer = ArtworkSerializer(artwork, context={"request":request})
        return Response(serializer.data)
    
    if request.method == "DELETE":
        artwork.delete()
        return Response(stauts=status.HTTP_204_NO_CONTENT)
    
    serializer = ArtworkSerializer(artwork, data=request.data, partial=request.method=="PATCH", context={"request":request})
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def artwork_star(request, art_id):
    artwork = get_object_or_404(Artwork, pk=art_id)
    if artwork.starred_by.filter(pk=request.user.pk).exists():
        artwork.starred_by.remove(request.user)
    else:
        artwork.starred_by.add(request.user)
    serializer = ArtworkSerializer(artwork, context={"request":request})
    return Response(serializer.data)