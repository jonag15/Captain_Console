from user.forms.registration import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.personal_info import PersonalInfo
from user.forms.personal_info import AddressInfo
from user.forms.payment_info import PaymentInfo
from user.models import UserImage
from user.models import Card
from user.models import Address
from user.forms.profile_form import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@login_required
def search_history(request):
    return render(request, 'user/search_history.html')

@staff_member_required
def admin_option(request):
    return render(request, 'user/admin_view.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

@login_required
def picture(request):
    profile = UserImage.objects.filter(customer_id=request.user.id).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/user/profile')
    return render(request, 'user/picture.html', {
        'form': ProfileForm(instance=profile)
    })

@login_required
def profile(request):
    if request.user.is_staff:
        return redirect('/user/admin-option')
    postform = User.objects.filter(id=request.user.id).first()
    address = Address.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        personalform = PersonalInfo(instance=postform, data=request.POST)
        if personalform.is_valid():
            postform.save()
            addressform = AddressInfo(instance=address, data=request.POST)
            if addressform.is_valid():
                address.save()
            return redirect('/user/profile')
    return render(request, 'user/profile.html', {
        'form': PersonalInfo(instance=postform),
        'address': AddressInfo(instance=address)
    })

@login_required
def change_payment(request):
    paymentInfo = Card.objects.filter(id=request.user.id).first()
    if request.method == 'POST':
        form = PaymentInfo(instance=paymentInfo, data=request.POST)
        if form.is_valid():
            paymentInfo.save()
            return redirect('/user/profile')
    return render(request, 'user/change_payment.html', {
        'form': PaymentInfo(instance=paymentInfo)
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("profile")
        else:
            return render(request, 'user/login.html', {})
    return render(request, 'user/login.html', {})


