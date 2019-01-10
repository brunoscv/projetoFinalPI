from django.urls import path
from timeline import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='exibir'),
    path('post/new', views.post_new, name='post_new'),

]