from django.urls import path
from .import views
app_name='master'

urlpatterns=[
  path('dash',views.dash,name='dash'),
  path('chart',views.chart,name='chart'),
  path('orders_view',views.orders_view,name='orders_view'),
  path('restaurants',views.restaurants,name='restaurants'),

]