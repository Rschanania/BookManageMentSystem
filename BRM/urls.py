from django.urls import path,include
from BRM import views

urlpatterns=[

    path('newBook',views.newBook),
    path('view-books',views.viewBook),
    path('edit-book',views.editBook),
    path('delete-book',views.deleteBook),
    path('search-book',views.searchBook),
    path(r'add',views.add),
    path('new-book',views.newBook),
    path('search',views.search),
    path('edit',views.edit),
    path('login',views.userLogin),
    path('logout',views.userLogout),
]