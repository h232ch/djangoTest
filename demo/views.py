import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Album, Track
from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework import generics
from .serializers import BookSerializer, AlbumSerializer, TrackSerializer


# def first(request):
#     return HttpResponse('First message from views')

# def first(request):
#     return render(request, 'first_temp.html', {'data': 'this is a data from views'})


class ClassBasedViewBooks(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        # return HttpResponse(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassBasedViewBookDetail(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MixingViewBooks(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MixingViewDetailBook(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view()
def function_based_view_books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def function_based_view_detail_book(request, pk):
    get_object = Book.objects.get(pk=pk)

    if not get_object:
        raise Http404
    elif request.method == 'GET':
        book = get_object
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        book = get_object
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book = get_object
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def first(request):
    books = Book.objects.all()
    # books = Book.objects.filter(is_published=True)
    return render(request, 'first_temp.html', {'books': books})


# class Another(View):
#     # books = Book.objects.all()
#     books = Book.objects.filter(is_published=True)
#     output = ''
#     for book in books:
#         output += f"We have {book.title} book with ID" \
#                   f" {book.id} <br>"
#
#     # output = f"We have {len(books)} that many books in DB"
#
#     # Selecting one object
#     book = Book.objects.get(id=5)
#
#     def get(self, request):
#         # return HttpResponse('This is another function inside class')
#         return HttpResponse(self.output)


# we need to study ViewSet more
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    # settings.py에 먼저 정의하더라도 아래 권한이 먼저 적용됨
    # permission_classes = (IsAuthenticated,)


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
