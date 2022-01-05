from rest_framework.pagination import PageNumberPagination


class MypageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'pageNum'
    page_size_query_param = 'rows'


