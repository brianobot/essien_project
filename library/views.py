from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Author, Department, Publisher
from itertools import chain
from django.db.models import Q

# Create your views here.
def home_page(request):
    if request.method == 'GET' and request.GET.get('search'):
        return redirect('library:search', request.GET.get('search'))
    book_list = Book.objects.all()[:9]
    context = {
        "books_list": book_list,
    }
    return render(request, 'library/Home.html', context)

def search_list(request, search_word):
    if request.method == 'GET' and request.GET.get('search'):
        return redirect('library:search', request.GET.get('search'))
    matched_books = Book.objects.filter(Q(title__icontains=search_word)|Q(author__name__icontains=search_word)|Q(dept__name__icontains=search_word)|Q(publisher__name__icontains=search_word)).distinct()

    context = {
        'search_list': matched_books,
        'search_word': search_word,
    }
    return render(request, 'library/search_list.html', context)