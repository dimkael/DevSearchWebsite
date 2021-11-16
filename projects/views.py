from django.shortcuts import render
from .models import Project


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully func ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Now i am trying to implemented social network'
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    proj = Project.objects.get(id=pk)
    context = {'project': proj}
    return render(request, 'projects/singleproject.html', context)