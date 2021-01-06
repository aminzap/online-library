from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
from django.core.paginator import Paginator


def bookList(request,page=1):
    book_list=models.Book.objects.published()
    paginator=Paginator(book_list, 3)
    book = paginator.get_page(page)
    contex = {"books": book,
              }
    return render(request, 'book/index.html', context=contex)


def singleBook(request, id):
    context = {"book": get_object_or_404(models.Book.objects.published(),id=id)}
    return render(request, 'book/post.html', context=context)
def category(request,slug):
    context={
        "category":get_object_or_404(models.Category,slug=slug ,status=True)
    }
    return render(request,"book/category.html",context=context)
