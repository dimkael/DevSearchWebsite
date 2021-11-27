from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchProjects(query):
    skills = Skill.objects.filter(name__icontains=query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=query) |
        Q(short_intro__icontains=query) |
        Q(skill__in=skills)
    )

    return profiles


def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)
    pages_num = 5

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    half_size = pages_num // 2
    leftIndex = int(page) - half_size
    if leftIndex <= 1:
        leftIndex = 1

    rightIndex = int(page) + half_size
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)
    print(custom_range)

    return custom_range, profiles
