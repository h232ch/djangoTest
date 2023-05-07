from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book, Album, Track
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .serializers import BookSerializer, AlbumSerializer, TrackSerializer


# def first(request):
#     return HttpResponse('First message from views')

# def first(request):
#     return render(request, 'first_temp.html', {'data': 'this is a data from views'})

def first(request):
    books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    return render(request, 'first_temp.html', {'books': books})


class Another(View):

    # books = Book.objects.all()
    books = Book.objects.filter(is_published=True)
    output = ''
    for book in books:
        output += f"We have { book.title } book with ID" \
                  f" { book.id } <br>"

    # output = f"We have {len(books)} that many books in DB"

    # Selecting one object
    book = Book.objects.get(id=2)

    def get(self, request):
        # return HttpResponse('This is another function inside class')
        return HttpResponse(self.output)


# we need to study ViewSet more
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()

