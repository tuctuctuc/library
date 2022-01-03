from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Индекс страница
def index(request):
    books =[
        {'title':'TOFR',
        'genre':'fantasy',
        'slug':'first-book'},
        {'title':'The thief',
        'genre':'roman',
        'slug':'second-book'}
    ]
    return render(request, 'books/index.html',{
        'show_books': True,
        'books':books})
