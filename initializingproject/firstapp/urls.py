from django.urls import path,include
from .views import *

urlpatterns = [
    path('', home),
    path('about',aboutus),
    path('Registration',Registration),
]