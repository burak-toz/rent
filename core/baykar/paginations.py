from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class SmallPagination(PageNumberPagination):
    page_size = 25

class MediumPagination(PageNumberPagination):
    page_size = 50

class LargePagination(PageNumberPagination):
    page_size = 100
