from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book_list/', views.book_list, name='book_list'),
    path('review_list/', views.review_list, name='review_list'),
    path('book_review_list/<int:book_id>/', views.book_review_list, name='book_review_list'),
    path('add_book', views.add_book, name='add_book'),
]
