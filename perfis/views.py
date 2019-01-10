from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from perfis.models import Perfil, Convite
from django.shortcuts import redirect
from django.views.generic.base import View
from usuarios.forms import MudarSenhaForm
from timeline.models import Post
from django.utils import timezone
from perfis.forms import PesquisaUsuarioForm, PostForm

@login_required
def index(request):
	posts = Post.objects.all().order_by('-created_date')
	return render(request, 'index.html',{'perfis' : Perfil.objects.all(),
										 'perfil_logado' : get_perfil_logado(request),
										 'posts': posts})

def exibir_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : get_perfil_logado(request)})

def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	
	if(perfil_logado.pode_convidar(perfil_a_convidar)):
		perfil_logado.convidar(perfil_a_convidar)
	
	return  redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(usuario=request.user)

def aceitar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')

def recusar(request, convite_id):
	convite = Convite.objects.get(id = convite_id)
	convite.recusar()
	return redirect('index')

def desfazer_amizade(request, perfil_id):
	perfil = get_perfil_logado(request)
	perfil.desfazer_amizade(perfil_id)
	return redirect('index')

from django.shortcuts import render

@login_required
def definirSuperUser(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil.usuario.is_superuser = True
    perfil.usuario.save()
    perfil.save()
    return redirect('index')


@login_required
def mudar_senha(request):

	form = MudarSenhaForm(request.POST or None)
	if form.is_valid():
		if request.user.check_password(form.cleaned_data['senha_antiga']):
			request.user.set_password(form.cleaned_data['nova_senha'])
			request.user.save()
		return redirect('index')
	return render(request, 'mudar_senha.html', {'form':form})

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
    return render(request, 'index.html', {'form': form})


class PesquisarPerfilView(View):
	def post(self, request):
		form = PesquisaUsuarioForm(request.POST)

		if form.is_valid():
			dados_form = form.cleaned_data
			perfil_logado = get_perfil_logado(request)
			perfis_acessiveis = perfil_logado.pesquisar(dados_form['nome'])

			return render(request, 'pesquisa.html',
						  {'perfis': perfis_acessiveis, 'perfil_logado': get_perfil_logado(request)})
