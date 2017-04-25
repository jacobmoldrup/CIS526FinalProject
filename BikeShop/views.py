from django.shortcuts import render

# Create your views here.
def post_main_page(request):
    return render(request, 'Layout/index.html', {})

def login(request):
    return render(request,'pages/login.html',{})

def bikes(request):
    return render(request,'pages/bikes.html',{})

def services(request):
    return render(request,'pages/services.html',{})
def favorites(request):
    return render(request, 'pages/favorites.html', {})

def cart(request):
    return render(request, 'pages/cart.html',{})