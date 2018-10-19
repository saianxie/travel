from django.urls import path
from django.conf.urls import url,include
from . import views
app_name = 'tripline'
urlpatterns = [
    url(r'^show/', views.show, name='show'),
    url(r'^addcountry/', views.add, name='add'),
    url(r'^gettimebytimeid\w*/(?P<timeid>\d*)/', views.gettime, name='gettime'),
    url(r'^getcountrybychauid\w*/(?P<chauid>\d*)/', views.getcountry, name='getcountry'),
    url(r'^gettraveldata\w*/', views.gettraveldata, name='gettraveldata'),
]
