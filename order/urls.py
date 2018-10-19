from django.urls import path
from django.conf.urls import url,include
from . import views
app_name = 'order'
urlpatterns = [
    url(r'^show/', views.show, name='show'),
]
