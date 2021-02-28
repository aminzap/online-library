from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models
from django.core.paginator import Paginator
from rest_framework import generics, permissions, mixins,exceptions
from . import serializers
from rest_framework.permissions import IsAdminUser


def bookList(request, page=1):
    book_list = models.Book.objects.published()
    paginator = Paginator(book_list, 3)
    book = paginator.get_page(page)
    contex = {"books": book,
              }
    return render(request, 'book/book list.html', context=contex)


def singleBook(request, id):
    context = {"book": get_object_or_404(models.Book.objects.published(), id=id)}
    return render(request, 'book/post.html', context=context)


def category(request, slug, page=1):
    category = get_object_or_404(models.Category, slug=slug, status=True)
    category_list = category.book.published()
    paginator = Paginator(category_list, 3)
    books = paginator.get_page(page)
    context = {'category': category,
               'books': books
               }
    return render(request, "book/category.html", context=context)


# api
class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        book = models.Book.objects.filter(pk=kwargs['pk'], creator=self.request.user)
        if book.exists():
            return self.destroy(request,*args,**kwargs)
        else:
            raise exceptions.ValidationError('no no no')