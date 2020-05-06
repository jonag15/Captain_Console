from django.shortcuts import render

products = [
    {'name': 'Tölvuleikur 1', 'price': 1000},
    {'name': 'Tölvuleikur 2', 'price': 1000},
    {'name': 'Tölvuleikur 3', 'price': 1000},
    {'name': 'Leikjatölva 1', 'price': 5000},
    {'name': 'Leikjatölva 2', 'price': 5000},

]

# Create your views here.
def index(request):
    return render(request, 'product/index.html', context={'products': products})

def info_index(request):
    return render(request, 'product/info.html')


