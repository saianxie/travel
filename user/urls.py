from django.urls import path
from django.conf.urls import url,include
from . import views
app_name = 'user'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('add/', views.addPosition, name='addPos'),
    url(r'^login/', views.login, name='login'),
    url(r'^regist\w*/', views.regist, name='regist')

]
