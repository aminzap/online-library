from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookList, name='list'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('single/<int:id>/', views.singleBook, name='single'),
    path('page/<int:page>/', views.bookList, name='list'),
]
