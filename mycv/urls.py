from django.urls import path
from mycv.views import index_view

app_name = 'mycv'

urlpatterns = [
    path('',index_view, name='index'),
]
