"""操作json"""
import os
import json
from django.conf import settings


class JsonMan():
    def __init__(self):
        self.dict = {}

    def parse_file(self, filename):
        """从文件中解析"""
        with open(os.path.join(settings.BASE_DIR, filename), 'r', encoding='utf-8') as jsonfile:
            self.dict = json.load(jsonfile)
        return self.dict

    def parse_text(self, jsontext):
        self.dict = json.loads(jsontext)
        return self.dict

    def get_dict(self):
        return self.dict


jsonman = JsonMan()