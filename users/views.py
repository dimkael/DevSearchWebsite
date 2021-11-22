from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, User


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')

    context = {'profile': profile, 'top_skills': top_skills, 'other_skills': other_skills}
    return render(request, 'users/user_profile.html', context)


def login_user(request):
    if request.user.is_authenticated:
        redirect('profiles')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.error(request, 'You are successfully logout')

    return redirect('login')
