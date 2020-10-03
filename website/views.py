from django.shortcuts import render
from .models import Post


def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'html',
             'Banco de dados', 'linux', 'Nginx', 'Uwsgi',
             'Systemctl']

    list_posts = Post.objects.all()

    data = {
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts}


    return render(request, 'indexgeral.html', data)
