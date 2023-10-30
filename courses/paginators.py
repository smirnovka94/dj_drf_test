from rest_framework.pagination import PageNumberPagination
class CoursePaginator(PageNumberPagination):
    page_size = 3  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания количества элементов на странице
    max_page_size = 100  # Максимальное количество элементов на странице
