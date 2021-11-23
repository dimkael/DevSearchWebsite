from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    proj = Project.objects.get(id=pk)
    context = {'project': proj}
    return render(request, 'projects/singleproject.html', context)


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    proj = profile.project_set.get(id=pk)
    form = ProjectForm(instance=proj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=proj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    proj = profile.project_set.get(id=pk)

    if request.method == 'POST':
        proj.delete()
        return redirect('projects')

    context = {'object': proj}
    return render(request, 'delete_template.html', context)