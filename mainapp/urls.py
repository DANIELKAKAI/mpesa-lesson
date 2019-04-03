from django.contrib import admin
from django.urls import path,include,re_path
from .views import index,mpesa_callback

urlpatterns = [
    re_path(r'^$',index,name="index"),
    path('mpesa-callback/',mpesa_callback,name='mpesa-callback')
]
