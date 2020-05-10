from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.personal_info import PersonalInfo
from user.models import Profile
from user.forms.profile_form import ProfileForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'user/index.html')


def new_user(request):
    return render(request, 'user/new_user.html')

def user_area(request):
    return render(request, 'user/user_area.html', context={ 'drasl': drasl })


def change_payment(request):
    return render(request, 'user/change_payment.html', context={ 'greidsluuppl': greidsluuppl})

def search_history(request):
    return render(request, 'user/search_history.html')

def register(request):
    print("Hér er POST")
    if request.method == 'POST':
        print("Eftir if post")
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def picture(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print("post")
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/')
    return render(request, 'user/picture.html', {
        'form': ProfileForm(instance=profile)
    })


def profile(request):
    form = User.objects.filter(id=request.user.id).first()
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=form)
    })