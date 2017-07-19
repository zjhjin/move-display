from django.test import TestCase
from app001.token import LoginTokenGenerator


class TokenGeneratorTestCase(TestCase):

    def setUp(self):
        self.ltg = LoginTokenGenerator()

    def test_make_token(self):
        token = self.ltg.make_token('zjhjin')
        self.assertEqual(len(token.split('.')), 3, '加密之后的数据是已 . 分割的耽搁字符串，格式正确')
        
    def test_check_token(self):
        token = self.ltg.make_token('zjhjin')
        self.assertEqual(self.ltg.check_token(token)["username"], 'zjhjin', '在期限内的数据，可以呗正确验证')