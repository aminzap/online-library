from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models


def bookList(request):
    contex = {"books": models.Book.objects.all(),
              }
    return render(request, 'book/index.html', context=contex)


def singleBook(request, id):
    context = {"book": models.Book.objects.get(id=id)}
    return render(request, 'book/post.html', context=context)
def category(request,slug):
    context={
        "category":get_object_or_404(models.Category,slug=slug ,status=True)
    }
    return render(request,"book/category.html",context=context)
