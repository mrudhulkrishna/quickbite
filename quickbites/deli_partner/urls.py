from django.urls import path
from .import views
app_name='deli_partner'

urlpatterns=[
  path('home',views.home,name='home')

]