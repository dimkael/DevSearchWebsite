from django.shortcuts import render
from .models import Project
from .forms import ProjectForm


def create_project(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    proj = Project.objects.get(id=pk)
    context = {'project': proj}
    return render(request, 'projects/singleproject.html', context)