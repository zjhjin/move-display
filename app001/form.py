from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist


# User = get_user_model()
from django.contrib.auth.models import User


class ParaCheckForm(forms.Form):
    """公用的参数验证"""
    source = forms.CharField()
    # type = forms.CharField()
    code = forms.CharField()
    data = forms.Field(required=False)


class ParaCheckFormBBX(ParaCheckForm):
    """验证佰宝箱提交的数据合法"""
    source = forms.CharField()


class ParaCheckFormAuto(ParaCheckForm):
    """验证佰宝箱提交参数的合法性"""
    source = forms.CharField()
    # type = forms.CharField()
    code = forms.CharField()
    data = forms.Field(required=False)


class LoginForm(forms.Form):
    """验证用户合法，并登陆view"""
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username = username)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                message="用户不存在",
                code=3000
            )
        if not authenticate(username=username, password=password):
            raise forms.ValidationError(
                message="用户登陆失败",
                code=3001
            )
        return self.cleaned_data
