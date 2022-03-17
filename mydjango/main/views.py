from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book, Review


def index(request):
    data = {
        'head': 'Дзен Python',
        'values': [
            'Красивое лучше уродливого.', 'Явное лучше неявного.', 'Простое лучше сложного.',
            'Сложное лучше запутанного.', 'Развернутое лучше вложенного.', 'Разреженное лучше плотного.',
            'Читаемость имеет значение.', 'Особые случаи не настолько особые, чтобы нарушать правила.',
            'При этом практичность важнее безупречности.', 'Ошибки не должны замалчиваться.',
            'Если не замалчиваются явно.', 'Встретив двусмысленность, отбрось искушение угадать.',
            'Должен существовать один - и, желательно, только один – очевидный способ сделать что - то.',
            'Хотя этот способ поначалу может быть и не очевиден, если вы не голландец.',
            'Сейчас лучше, чем никогда.', 'Хотя никогда часто лучше, чем * прямо * сейчас.',
            'Если реализацию сложно объяснить – идея точно плоха.',
            'Если реализацию легко объяснить-возможно, идея хороша.',
            'Пространства имен – отличная штука! Будем использовать их чаще!'
        ]
    }
    return render(request, 'main/index.html', data)

def book_detail(request, book_id):
    #return HttpResponse(f'Your book id is {book_id}')
    book = Book.objects.get(id=book_id)
    review = Review.objects.all()
    return render(request, 'main/book_detail.html', {'book_id': book_id, 'book': book, 'review': review})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'main/book_list.html', {'books': books})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'main/review_list.html', {'reviews': reviews})

def book_review_list(request, book_id):
    reviews = Review.objects.filter(book=book_id)
    return render(request, 'main/book_review_list.html', {'book_id': book_id, 'reviews': reviews})

def add_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect('book_list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookForm()

    return render(request, 'main/book_form.html', {'form': form})


