from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    proj = Project.objects.get(id=pk)
    form = ProjectForm(instance=proj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def delete_project(request, pk):
    proj = Project.objects.get(id=pk)

    if request.method == 'POST':
        proj.delete()
        return redirect('projects')

    context = {'object': proj}
    return render(request, 'projects/delete_template.html', context)


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    proj = Project.objects.get(id=pk)
    context = {'project': proj}
    return render(request, 'projects/singleproject.html', context)