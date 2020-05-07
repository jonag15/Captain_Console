from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def search_history(request):
    return render(request, 'user/search_history.html')