from rest_framework.pagination import PageNumberPagination
class LessonPaginator(PageNumberPagination):
    page_size = 3  # Количество элементов на странице
