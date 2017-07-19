"""一切项目中所需要的数据模版都在此提供"""
import copy
import functools
from django.conf import settings
from libstore.jsonman import jsonman


@functools.lru_cache()
def response_template(code, message=None):
    code_message = jsonman.parse_file("djangoprj/code_msg_conf.json")
    code = int(code)
    response = copy.copy(settings.RESPONSE_JSON_TEMP)
    response["code"] = code
    response["message"] = (message or '') + code_message[str(code)]
    return response
