from django.urls import path
from . views import *

urlpatterns =[
    path('user_detail',UserDetailsAPI.as_view(),name='user_details'),
    path('register',RegisterUserAPI.as_view(),name='register')
]