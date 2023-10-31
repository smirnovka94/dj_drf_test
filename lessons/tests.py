from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from courses.models import Course
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


    def test_get_list(self):
        """Test of getting list of Lessons"""
        response = self.client.get(
            '/lesson/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_lesson(self):
        """Test of creating list of Lessons"""
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
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )