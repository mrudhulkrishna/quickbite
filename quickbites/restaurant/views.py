from razorpay import Order
from customer.models import OrderItem
from quickbites import settings
from restaurant.models import Menu
from django.shortcuts import redirect, render

from restaurant.models import Category
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'restaurant/home.html')

def add_category(request):
    msg=''
    if request.method=='POST':
        acat_name = request.POST['cat_name']
        adiscription = request.POST['discription']
        restaurantid=request.session['restaurant_id']

        new_category = Category(catg_name = acat_name, discription = adiscription,restaurant_id=restaurantid)

        new_category.save()

        msg='category added successfuly'
    return render(request,'restaurant/add_category.html',{'status':msg}) 
   
def view_category(request):

    category=Category.objects.filter(restaurant_id=request.session['restaurant_id'])
    return render(request,'restaurant/view_category.html',{'category':category}) 
 
def edit_category(request,id):

    category=Category.objects.get(id=id)

    if request.method=='POST':
        ecat_name = request.POST['cat_name']
        ediscription = request.POST['discription']
        restaurantid=request.session['restaurant_id']

        up_category= Category.objects.filter(id=id).update(catg_name=ecat_name,discription=ediscription, restaurant_id=restaurantid)
        
        return redirect('restaurant:view_category')
    return render(request,'restaurant/edit_category.html',{'category':category}) 

def delete_category(request,id):

    delete_cat=Category.objects.get(id=id)
    delete_cat.delete()
    msg='deleted'
    category=Category.objects.filter(restaurant_id=request.session['restaurant_id'])

    return render(request,'restaurant/view_category.html',{'status':msg,'category':category})
  
def add_menu(request):

    category=Category.objects.filter(restaurant_id=request.session['restaurant_id'])
    msg=''
    if request.method=='POST':
       mitem_name=request.POST['item_name']
       mcategory=request.POST['category']
       mfood_type=request.POST['food_type']
       mprice=request.POST['price']
       mimage=request.FILES['image']  
       restaurantid=request.session['restaurant_id']

       new_menu=Menu(item_name =mitem_name, category_id = mcategory, price = mprice, food_type = mfood_type,
                         image = mimage, restaurant_id = restaurantid)

       new_menu.save()

       msg='Menu added successfuly'  
    return render(request,'restaurant/add_menu.html',{'status':msg,'category':category}) 

def view_menu(request):

    menu=Menu.objects.filter(restaurant_id=request.session['restaurant_id']) 
    return render(request,'restaurant/view_menu.html',{'menu':menu}) 

def edit_menu(request,id):

    menu=Menu.objects.get(id=id)
    category=Category.objects.filter(restaurant_id=request.session['restaurant_id'])
    current_category_ids=category.values_list('id',flat=True)

    if request.method=='POST':
       mitem_name=request.POST['item_name']
       mcategory=request.POST['category']
       mfood_type=request.POST['food_type']
       mprice=request.POST['price']
       mimage=request.FILES['image']  
       restaurantid=request.session['restaurant_id']

       UP_menu=Menu.objects.filter(id=id).update(item_name = mitem_name, category_id = mcategory, food_type = mfood_type, price = mprice,
                             image = mimage, restaurant_id = restaurantid)
    
       return redirect('restaurant:add_menu')
    context={
        'menu':menu,
        'category':category,
        'current_category':current_category_ids
        }
    
    return render(request,'restaurant/edit_menu.html',context) 

def delete_menu(request,id):

    mdelete=Menu.objects.get(id=id)
    mdelete.delete()
    msg='deleted'
    menu=Menu.objects.filter(restaurant_id=request.session['restaurant_id'])

    return render(request,'restaurant/view_menu.html',{'status':msg,'menu':menu}) 

def orders(request):
    restaurant_id=request.session['restaurant_id']
    order_items =OrderItem.objects.filter(menu__restaurant_id=restaurant_id).select_related('order','menu')
    orders={}
    for order_item in order_items:
        order =order_item.order
        if order not in orders:
            orders[order]=[]
        orders[order].append(order_item)


    if request.method=='POST':
        order_id=request.POST['order_id']
        action=request.POST['action']

        order=Order.objects.get(id=order_id)
        if action=='confirm':
            send_mail(
                "Order Confirmation",
                "your order has been confirmed . Thank you for purchase . orderid :"+order_id,
                settings.EMAIL_HOST_USER,
                ['mrudhulkrishnamp65@gmail.com'],
                fail_silently=False
            )
            order.order_status='confirmed'
            order.save()
        elif action=='reject':
            send_mail(
                "Order Rejection",
                "your order has been rejected . orderid :"+order_id,
                settings.EMAIL_HOST_USER,
                ['mrudhulkrishnamp65@gmail.com'],
                fail_silently=False
            )
            order.order_status='rejected'
            order.save()

    
    context={
        'orders':orders
    }
    return render(request,'restaurant/orders.html',context) 



