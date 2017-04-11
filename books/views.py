# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Book

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }

    return render(request, 'books/index.html', context)

def detail(request, book_id):
    return HttpResponse("<h2> Details for book id " + str(book_id)+ "</h2>")

def special(request):
    return HttpResponse('You are special')