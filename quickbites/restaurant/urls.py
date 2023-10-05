from django.urls import path
from .import views
app_name='restaurant'

urlpatterns=[
  path('home',views.home,name='home'),
  path('add_category',views.add_category,name='add_category'),
  path('view_category',views.view_category,name='view_category'),
  path('add_menu',views.add_menu,name='add_menu'),
  path('view_menu',views.view_menu,name='view_menu'),
  path('orders',views.orders,name='orders'),
  path('edit_category/<int:id>',views.edit_category,name='edit_category'),
  path('delete/<int:id>',views.delete_category,name='delete'),
  path('edit_menu/<int:id>',views.edit_menu,name='edit_menu'),
  path('delete_menu/<int:id>',views.delete_menu,name='delete_menu'),

  
]