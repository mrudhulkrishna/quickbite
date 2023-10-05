from django.urls import path
from .import views
app_name='customer'

urlpatterns=[
  path('home',views.home,name='home'),
  path('cart',views.cart,name='cart'),
  path('add_cart/<int:mid>',views.add_cart,name='add_cart'),
  path('remove_cart',views.remove_cart,name='remove_cart'),
  path('update_quantity',views.update_quantity,name='update_quantity'),
  path('order_menu',views.order_menu,name='order_menu'),
  path('updatepayment',views.updatepayment,name='updatepayment'),
  path('order_history',views.order_history,name='order_history'),
  path('cancel_order/<int:item_id>',views.cancel_order,name='cancel_order'),
 
]