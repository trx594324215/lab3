from django.http import HttpResponse
from books.models import Book
from django.shortcuts import render_to_response
#the main page


def home(request):
    errors = []
    book=Book.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20characters.')
        else:
            #name = Book.AuthorsID.Name
            books = Book.objects.filter(AuthorsID__Name__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q, 'Book': book})
    return render_to_response('home_page.html',
        {'errors': errors, 'Book': book})
    
    
