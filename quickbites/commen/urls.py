from django.urls import path
from .import views
app_name='commen'

urlpatterns=[
  path('home',views.home,name='home'),
  path('admin_log',views.admin_log,name='admin_log'),
  path('admin_sign',views.admin_sign,name='admin_sign'),
  path('restaurant_log',views.restaurant_log,name='restaurant_log'),
  path('restaurant_sign',views.restaurant_sign,name='restaurant_sign'),
  path('customer_log',views.customer_log,name='customer_log'),
  path('customer_sign',views.customer_sign,name='customer_sign')

]