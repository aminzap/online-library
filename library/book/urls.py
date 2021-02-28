from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.bookList, name='list'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('single/<int:id>/', views.singleBook, name='single'),
    path('page/<int:page>/', views.bookList, name='list'),
    path('category/<slug:slug>/page/<int:page>/', views.category, name='category'),

    # api
    path('api/BookList/', views.BookList.as_view(), name='book-list'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/DelAndUpdateBook/<int:pk>/',views.BookRetrieveUpdateDestroy.as_view(),name='del-and-update-book'),
]
