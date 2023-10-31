from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from courses.models import Course
from lessons.models import Lesson
from users.models import User


class LessonsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            email='user@test.com',
            number='123456789',
            city='Msc',
            role='MEMBER'
        )
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем
        self.user.set_password('ghjtrn88')
        self.user.save()

        self.course = Course.objects.create(
            name="FirstCorse",
            content="Bla-bla www.youtube.com bla-bla-bla",
            name_user=self.user)

        self.lesson = Lesson.objects.create(
            name="Test",
            content="Test content",
            name_user=self.user)



    def test_create_lesson(self):
        """Тест создание урока"""
        data={
            "name": "7 lesson",
            "content": "moderator",
            "course": self.course.id,
            "name_user": self.user.id,
            "url": "https://www.youtube.com"
        }
        response = self.client.post(
            reverse('lessons:lesson_create'),
            data=data
        )
        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_get_list(self):
        """Тест чтение списка уроков """
        response = self.client.get(
            '/lesson/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_number(self):
        """Тест чтение экземпляра урока"""

        response = self.client.get(
            reverse('lessons:lesson_get', args=[self.lesson.id]))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_number_update(self):
        """Тест Обновление  экземпляра урока"""
        data = {
            "name": "New test",
            "content": "New Test content",
            "course": self.course.id,
            "name_user": self.user.id,
            "url": "https://www.youtube.com"
        }
        response = self.client.patch(
            reverse('lessons:lesson_update', args=[self.lesson.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_number_delete(self):
        """Тест удаление  экземпляра урока"""

        response = self.client.delete(
            reverse('lessons:lesson_delete', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
