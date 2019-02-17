from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^c2viwer/$', views.c2List.as_view(), name='c2-list'),

]