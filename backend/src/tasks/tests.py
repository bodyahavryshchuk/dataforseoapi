from django.urls import reverse
from rest_framework.test import APITestCase

from src.tasks import models


class ProfileTest(APITestCase):
    def setUp(self):
        self.task1 = models.Task.objects.create(
            id='04021358-2713-0066-0000-bd5be11b2e02',
            status_code=20100,
            status_message='Task Created.',
            time='0.56',
            cost=0.00005
        )
        self.task_data1 = models.TaskData.objects.create(
            task=self.task1,
            api=20100,
            function='Task Created.',
            se='google',
            se_type='0.56',
            language_code='0.56',
            location_code='0.56',
            keyword='0.56',
            device='0.56',
            os='0.56',
        )

    def test_task_list(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        data = {
            'engine': 'google',
            'location': '21146',
            'keyword': 'hello',
        }
        response = self.client.post(reverse('task_create'), data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_task_data(self):
        response = self.client.get(reverse('task_data'))
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, 200)

    def test_task_result(self):
        response = self.client.get(reverse('task_result', kwargs={'se': self.task_data1.se,
                                                                  'pk': self.task_data1.task}
                                           ))
        self.assertEqual(response.status_code, 200)

    #    python manage.py test src
