from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book,Author
#for all the views


def more(request):
    ID = request.GET['ID']
    #D = request.GET.get('D')
    #D = []
    #if not D:
        #Book.objects.filter(ID__icontains=ID).delete()
        #D=[]
        #return render_to_response('test.html')
    #else:
    book = Book.objects.filter(ISBN__icontains=ID)
    return render_to_response('more.html',{'q':book[0], 'a':book[0].AuthorsID.Name})

def delete(request):
    ID = request.GET['D']
    Book.objects.filter(ISBN__icontains=ID).delete()
    return render_to_response('test.html')

def edit(request):
    errors = []
    ID = request.GET['D']
    books = Book.objects.filter(ISBN__icontains=ID)
    book = books[0]
    #authorss = Author.objects.all()
    #authors = authorss[0]
    if 'Publisher' and 'Publishdate' and 'Price' in request.GET:
        publisher = request.GET['Publisher']
        price = request.GET['Price']
        publishdate = request.GET['Publishdate']
        #author = request.GET['Author']
        return render_to_response('edit.html',{'errors':errors, 'Book':book,'D':book.ISBN,'Publisher':publisher,'Publishdate':publishdate,'Price':price})
    return render_to_response('edit.html',{'errors':errors, 'Book':book, 'D':ID})

def after(request):
    ID = request.GET['D']
    if 'Publisher' in request.GET:
        publisher = request.GET['Publisher']
        if publisher:
            Book.objects.filter(ISBN__icontains=ID).update(Publisher=publisher)
            #return render_to_response('test.html')
    if 'Publishdate' in request.GET:
        publishdate = request.GET['Publishdate']
        if publishdate:
            Book.objects.filter(ISBN__icontains=ID).update(PublishDate=publishdate)
    if 'Price' in request.GET:
        price = request.GET['Price']
        if price:
            Book.objects.filter(ISBN__icontains=ID).update(Price=price)
    return render_to_response('edit.html')

def add(request):
    errors = []
    #authorss = Author.objects.all()
    #authors = authorss[0]
    if 'D' and 'Publisher' and 'Publishdate' and 'Price' in request.GET:
        publisher = request.GET['Publisher']
        price = request.GET['Price']
        publishdate = request.GET['Publishdate']
        #author = request.GET['Author']
        return render_to_response('edit.html',{'errors':errors, 'Book':book,'D':book.ISBN,'Publisher':publisher,'Publishdate':publishdate,'Price':price})
    return render_to_response('edit.html',{'errors':errors, 'Book':book})
