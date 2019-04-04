from django.contrib import admin
from django.urls import path,include,re_path
from .views import *

urlpatterns = [
    re_path(r'^$',index,name="index"),
    path('b2c/mpesa-callback/',mpesa_callback,name='b2c-callback'),
    path('c2b/confirmation/',c2b_confirmation,name='c2b-confirmation'),
    path('c2b/validation_url/',c2b_validation,name='c2b-validation')
]
