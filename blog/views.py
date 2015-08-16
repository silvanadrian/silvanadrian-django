from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from .models import Post,Tag

# Create your views here.

def post_list(request):
    blogposts = Post.objects.all().filter(is_public=True)
    tags = Tag.objects.all()
    context = {'blogposts': blogposts}
    return render(request, 'blog/post_list.html',context)

def view_post(request, slug):
    return render_to_response('blog/view_post.html', {
    'post': get_object_or_404(Post, slug=slug)
    })