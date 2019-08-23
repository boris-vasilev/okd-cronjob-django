from django.conf.urls import url
from . import views

urlpatterns = [
    url('hello', views.hello, name='hello'),
]
