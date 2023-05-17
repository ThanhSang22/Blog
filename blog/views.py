from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def list(request):
    post = Post.objects.all().order_by("-date")

    paginator = Paginator(post, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/blog.html", {'page_obj': page_obj})


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {"post": post})
