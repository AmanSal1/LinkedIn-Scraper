import unittest
from unittest.mock import patch, MagicMock
from app import app


class LinkedInScraperTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.genai.GenerativeModel')
    @patch('app.login_to_linkedin')
    @patch('app.scrape_posts')
    def test_scrape(self, mock_scrape_posts, mock_login_to_linkedin, mock_genai_model):
        mock_driver = MagicMock()
        mock_login_to_linkedin.return_value = mock_driver

        mock_scrape_posts.return_value = [
            "Post 1 content",
            "Post 2 content",
            "Post 3 content",
            "Post 4 content",
            "Post 5 content"
        ]

        mock_model_instance = mock_genai_model.return_value
        mock_model_instance.generate_content.return_value = MagicMock(text="Custom connection message.")

        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'profileUrl': 'https://www.linkedin.com/in/test-profile'
        }

        response = self.app.post('/scrape', data=data)

        self.assertEqual(response.status_code, 200)

        response_json = response.get_json()
        self.assertIn('message', response_json)
        self.assertIn('posts', response_json)
        self.assertEqual(len(response_json['posts']), 5)
        self.assertEqual(response_json['message'], "Custom connection message.")

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)


if __name__ == '__main__':
    unittest.main()
