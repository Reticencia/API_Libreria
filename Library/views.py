from django.shortcuts import render
from rest_framework import generics,status
from .serializer import BookSerializer
from .pagination import BookPagination
from .models import Book
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
'''
class AddBookAllBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-published_date')
    serializer_class = BookSerializer
    pagination_class = BookPagination

#La forma en la que se puede buscar y aplicar filtros en DRF 
#Documentacion:
class SearchBook(generics.ListAPIView):

    serializer_class = BookSerializer

    def get_queryset(self):

        author = self.kwargs['author']
        return Book.objects.filter(author = author)

Este codigo utlizo para filtrar y edito el queryset, esto es basicamente una colecion de registros de la DB
esto es para entrar 

'''


