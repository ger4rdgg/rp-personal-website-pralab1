from django.shortcuts import render
from apps.blog import models

# Create your views here.
def post_list(request):
    posts= models.Post.objects.all().order_by('-created_on')

    context = {
        'posts':posts

    }
     return render(request, 'post_list.html', context)
