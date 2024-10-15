from django.urls import path
from devtest.views import device_test, home

urlpatterns = [
    path('', home, name='home'),
    path('device-test/', device_test, name='device_test'),
]
