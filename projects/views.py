from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from .models import Project,Update
# Create your views here.

def project_list(request):
    projects = Project.objects.all().filter(is_public=True)
    context = {'projects': projects}
    return render(request, 'projects/project_list.html',context)


def home(request):
    projects = Project.objects.all().filter(is_public=True)[:5]
    context = {'projects': projects}
    return render(request, 'projects/featured_projects.html',context)


def view_project(request, slug):
    return render_to_response('projects/view_project.html', {
        'project': get_object_or_404(Project, slug=slug)
    })