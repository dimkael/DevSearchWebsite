from django.db.models import Q
from .models import Profile, Skill


def searchProjects(query):
    skills = Skill.objects.filter(name__icontains=query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=query) |
        Q(short_intro__icontains=query) |
        Q(skill__in=skills)
    )

    return profiles