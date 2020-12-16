from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookList, name='list'),
    path('single/<int:id>/', views.singleBook, name='single'),
]
