from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm, LoginForm, RegisterForm, ReviewForm, EditBookDescriptionForm
from .models import Book, Review


def index(request):
    return render(request, 'main/index.html')

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

@login_required
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

@login_required
def edit_book(request, book_id):
    if request.method == 'POST':
        form = EditBookDescriptionForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(Book, pk=book_id)
            book.description = form.cleaned_data["description"]
            book.save()
            return redirect('book_detail', book.id)
    else:
        form = EditBookDescriptionForm()
        return render(request, 'main/book_.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login_form.html', {'form': form})

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            print(form.errors)
        return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()
        return render(request, "main/register_form.html", {"form": form})

def logout_user(request):
    logout(request)
    return HttpResponse('Logged out')

@login_required
def add_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            book = Book.objects.get(id=book_id)
            Review.objects.create(book=book, user=user, **form.cleaned_data)
            return redirect('book_review_list', book.id)
    else:
        form = ReviewForm()
        return render(request, 'main/review_form.html', {'form': form})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    if review.user == user:
        review.delete()
        return redirect('book_review_list', review.book.id)
    return HttpResponse('You can delete only your reviews!')


@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            review = get_object_or_404(Review, pk=review_id)
            if review.user == user:
                review.text = form.cleaned_data["text"]
                review.save()
                return redirect('book_review_list', review.book.id)
            return HttpResponse('You can edit only your reviews!')
    else:
        form = ReviewForm()
        return render(request, 'main/book_form.html', {'form': form})
