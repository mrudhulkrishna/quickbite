from django.shortcuts import render

# Create your views here.

def dash(request):
    return render(request,'master/dash.html') 
def chart(request):
    return render(request,'master/chart.html')
def orders_view(request):
    return render(request,'master/orders_view.html')
def restaurants(request):
    return render(request,'master/restaurants.html')
 

