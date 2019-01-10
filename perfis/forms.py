from django.forms import ModelForm
from perfis.models import *
from django.db import models
from django import forms
from timeline.models import Post

class PesquisaUsuarioForm(forms.Form):
    nome = forms.CharField(required=True)


class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('title', 'text',)

