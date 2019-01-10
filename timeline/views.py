from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from perfis.models import Perfil
from timeline.models import Post
from django.utils import timezone

from .forms import PostForm

def index(request):
   #return render(request, 'timeline/index.html', {})
   posts = Post.objects.all()
   return render(request, 'timeline/posts.html', {'posts': posts})



def exibir_posts(request):

    posts = Post.objects.filter(author_id=request.user.id)
    return render(request, 'timeline/posts.html', {'posts': posts})

def get_perfil_logado(request):
	return Perfil.objects.get(id=request.user.id)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'timeline/post_edit.html', {'form': form})


