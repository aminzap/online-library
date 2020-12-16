from django.shortcuts import render
from . import models


def bookList(request):
    contex = {"books": models.Book.objects.all(),
              "category": models.Category.objects.filter(status=True)}
    return render(request, 'book/index.html', context=contex)


def singleBook(request, id):
    context = {"book": models.Book.objects.get(id=id)}
    return render(request, 'book/post.html', context=context)
