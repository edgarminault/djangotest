from django.shortcuts import render
from projects.models import Project


def project_index(request):
    """
    PROJECT INDEX Page:
    -----------------------
    Returns all projects in a cards layout.
    """
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    """
    PROJECT DETAIL Page:
    Returns a detailed page of a project. Is an output page when clicking on a project
    in the index page.
    """
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)
