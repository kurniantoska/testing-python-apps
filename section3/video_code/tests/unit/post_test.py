from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Tes', 'Ini konten tes')

        self.assertEqual('Tes', p.title)
        self.assertEqual('Ini konten tes', p.content)

    def test_json(self):
        p = Post('Tes', 'Tes Konten')

        self.assertDictEqual({'title': p.title, 'content': p.content}, p.json())
