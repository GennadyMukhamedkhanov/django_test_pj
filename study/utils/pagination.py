from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 5  # Количество объектов на странице по умолчанию
    page_size_query_param = "page_size"  # Параметр запроса для указания количества объектов на странице
    max_page_size = 100  # Максимальное количество объектов на странице
