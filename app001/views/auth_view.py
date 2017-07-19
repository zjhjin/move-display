import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app001.form import LoginForm
from django.contrib.auth import authenticate
from app001.token import LoginTokenGenerator as token_generator
from libstore.templateparse import response_template
# Create your views here.


@csrf_exempt
def login(request):
    """登陆用户"""
    try:
        assert request.content_type == 'application/json'
    except AssertionError as e:
        print(e)
        '''返回需要的文件'''

    if request.method == "POST":
        request_args = json.loads(request.body, encoding="utf-8")

        form = LoginForm(request_args["data"])
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user:
                token = token_generator().make_token(request.user.username)
                context = response_template(100, '获取token')
                context["data"] = {"token": token}

            else:
                context = response_template(10000)
        else:
            context = response_template(10001, '【调试中】用户信息错误，导致')
        return JsonResponse(context)
