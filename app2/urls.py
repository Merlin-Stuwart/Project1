from django.urls import path
from app2.views import *
app_name='h1'
urlpatterns=[
    path('html1/',html1,name='html1')
]
