from user.forms.registration import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.personal_info import PersonalInfo
from user.forms.personal_info import AddressInfo
from user.forms.payment_info import PaymentInfo
from user.models import UserImage
from user.models import Card
from user.models import Profile
from user.models import Address
from django.contrib import messages
from user.models import Address
from product.models import SearchHistory
from user.forms.profile_form import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from product.forms.product_form import Product

# Create your views here.

@login_required
def search_history(request):
    context = {'products': Product.objects.filter(searchhistory__profile=request.user.id)}
    return render(request, 'user/search_history.html', context)

@staff_member_required
def admin_option(request):
    return render(request, 'user/admin_view.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nýskráning tókst!')
            return redirect('login')
        else:
            messages.info(request, 'Eitthvað fór útskeyðis. Annað hvort var lykilorðið of einfalt,'
                                   ' eða þá að það var ekki ritað nákvæmlega eins í bæði skiptin.')
            return render(request, 'user/register.html')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

@login_required
def picture(request):
    profile = UserImage.objects.filter(user_id=request.user.id).first()
    if profile == None:
        profile = UserImage()
        profile.user = request.user
        profile.image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/1024px-User_icon_2.svg.png'
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
    findprofile = Profile.objects.filter(user_id=request.user.id).first()
    if findprofile == None:
        print("No profile found, making one..")
        tempprofile = Profile()
        tempprofile.user = request.user
        tempprofile.save()
    findpicture = UserImage.objects.filter(user_id=request.user.id).first()
    if findpicture == None:
        findpicture = UserImage()
        findpicture.user = request.user
        findpicture.save()
    if request.user.is_staff:
        return redirect('/user/admin-option')
    postform = User.objects.filter(id=request.user.id).first()
    address = Address.objects.filter(user_id=request.user.id).first()
    if address == None:
        address = Address()
        address.user = request.user
        address.address = None
        address.zip_code = None
        address.city = None
        address.country = None
    if request.method == 'POST':
        personalform = PersonalInfo(instance=postform, data=request.POST)
        if personalform.is_valid():
            postform.save()
            addressform = AddressInfo(instance=address, data=request.POST)
            if addressform.is_valid():
                print(address.id)
                address.save()
                messages.success(request, 'Form submission successful')
            return redirect('/user/profile')
    return render(request, 'user/profile.html', {
        'form': PersonalInfo(instance=postform),
        'address': AddressInfo(instance=address)
    })

@login_required
def change_payment(request):
    paymentInfo = Card.objects.filter(id=request.user.id).first()
    if paymentInfo == None:
        paymentInfo = Card()
        paymentInfo.user = request.user
        paymentInfo.card_number = None
        paymentInfo.valid_month = None
        paymentInfo.valid_year = None
        paymentInfo.cvc = None
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


