from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from .forms import NameForm
# Create your views here.

def home(request):
    form = NameForm(request.POST or None)
    return render(request,'users/home.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')

@csrf_protect
def register(request):
    form = NameForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}')
            form.save()
            # url = 'https://www.facebook.com/'
            return redirect('/login')
    return render (request, 'users/register.html', {'form': form})


