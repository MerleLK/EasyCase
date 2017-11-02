from rest_framework.test import APITestCase
from rest_framework import status

from simpleblog.models import Tag


class TagTest(APITestCase):

    def setUp(self):
        Tag.objects.create(
            name='tag1',
        )
        Tag.objects.create(
            name='tag2',
        )

    def test_get_all_tag(self):
        r = self.client.get(
            '/api/tags',
        )
        self.assertEqual(
            r.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(r.data),
            2
        )

    def test_get_first_tag(self):
        r = self.client.get(
            '/api/tags/3',
        )
        self.assertEqual(
            r.status_code,
            status.HTTP_200_OK
        )
        print(r.data)
        self.assertEqual(
            'tag1',
            r.data.get('name')
        )
