from blog import Blog
from unittest import TestCase


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('judul blog', 'penulis')
        self.assertEqual('judul blog', b.title)
        self.assertEqual('penulis', b.author)
        self.assertEqual(0, len(b.posts))
        self.assertListEqual([], b.posts)

    def test_json_blog_no_post(self):
        b = Blog('judul blog', 'penulis')
        self.assertDictEqual(b.json(), {
            'title': b.title,
            'author': b.author,
            'posts': b.posts,
        })
