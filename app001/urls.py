from django.conf.urls import url
from . import views

app_name = "app001"

urlpatterns = [
    url("^$", view=views.home, name='home'),
    url("^token", view=views.get_token, name='token')
]

