from django.shortcuts import redirect, render

from commen.models import Admin, Customer, Restaurant
import restaurant

# Create your views here.

def home(request):
     return render(request,'commen/home.html')

def admin_log(request):
     msg=''
     if request.method=='POST':
        aemail=request.POST['email']
        apassword=request.POST['password']

    
        admin_log=Admin.objects.get(email=aemail,password=apassword)
        request.session['restaurant_id']=admin_log.id
        return redirect('master:dash')
    
     return render(request,'commen/admin_log.html',{'status':msg})

def admin_sign(request):
     return render(request,'commen/admin_sign.html')

def restaurant_log(request):
     msg=''
     if request.method=='POST':
        lemail=request.POST['email']
        lpassword=request.POST['password']

     #    try:
        restaurant=Restaurant.objects.get(email=lemail,password=lpassword)
        request.session['restaurant_id']=restaurant.id
        return redirect('restaurant:home')
     #    except:

     msg='invalide username or password'
     return render(request,'commen/restaurant_log.html',{'status':msg})

def restaurant_sign(request):
     msg = ''
     if request.method == 'POST':
        rname = request.POST['name']
        remail = request.POST['email']
        rphone = request.POST['phone']
        rpassword = request.POST['password']
        raddress = request.POST['address']
        racc_no = request.POST['acc_no']
        rifsc = request.POST['ifsc']
        rbranch = request.POST['branch']

        new_restaurant = Restaurant(name = rname, email = remail, phone = rphone,
                            password = rpassword, address = raddress, ac_no = racc_no,
                            ifsc = rifsc, branch = rbranch)
        new_restaurant.save()
        msg = " restaurant added succesfully"
     return render(request,'commen/restaurant_sign.html',{'status':msg})

def customer_log(request):
    msg=''
    if request.method=='POST':
        cemail=request.POST['email']
        cpassword=request.POST['password']

        # try:
        customer=Customer.objects.get(email=cemail,password=cpassword)
        request.session['customer_id']=customer.id
        return redirect('customer:home')
        # except:
    msg='invalide username or password'
    return render(request,'commen/customer_log.html',{'status':msg})  
 
def customer_sign(request):
    msg = ''
    if request.method == 'POST':
        cfirst = request.POST['first']
        clast = request.POST['last']
        cemail = request.POST['email']
        cpassword =request.POST['password']
        caddress = request.POST['address']
        caddress2 = request.POST['address2']
        ccity = request.POST['city']
        cstate = request.POST['state']
        ccountry = request.POST['country']

        new_customer = Customer(first = cfirst, last = clast, email= cemail, password = cpassword,
                                address = caddress, address2 = caddress2, city = ccity, state = cstate,
                                country = ccountry)
        new_customer.save()
        msg = "Customer Added Succesfully"   
    return render(request,'commen/customer_sign.html',{'status':msg})    