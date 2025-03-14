from rest_framework import pagination

class BookPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'size'
    max_page_size = 1000
