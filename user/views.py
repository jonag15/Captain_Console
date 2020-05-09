from django.shortcuts import render

# Test gögn, fer í ruslið                                                                       MUNA AÐ HENDA
drasl = [
    { 'name': 'Unnar Sigurðsson', 'email': 'bla@bla.is', 'phoneNumber': '7713712', 'address': 'Sólheimar 30', 'zipCode': '104', 'country': 'Ísland', 'picture': 'images/mynd.png'},
]

greidsluuppl = [
    { 'cardnum': '123123', 'exp': '03/23', 'cvc': '123'}
]

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def search_history(request):
    return render(request, 'user/search_history.html')

def new_user(request):
    return render(request, 'user/new_user.html')

def user_area(request):
    return render(request, 'user/user_area.html', context={ 'drasl': drasl })

def change_payment(request):
    return render(request, 'user/change_payment.html', context={ 'greidsluuppl': greidsluuppl})

def admin_option(request):
    return render(request, 'user/admin_view.html')
