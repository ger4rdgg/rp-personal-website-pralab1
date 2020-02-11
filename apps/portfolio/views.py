from django.shortcuts import render

# Create your views here.
from .models import project
def project_list(request):
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'project_list.html', context)
