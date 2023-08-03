from django.test import TestCase
from rest_framework.test import APIClient


class YourAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # 事前にテストデータをセットアップする場合はここで行う

    def test_your_api_endpoint(self):
        # テストコードをここに記述する
        response = self.client.get("/your-api-endpoint/")
        self.assertEqual(response.status_code, 200)
        # 他のテストアサーションも追加する
