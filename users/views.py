from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from .forms import NameForm
from django.contrib import messages
# Create your views here.

from .requesting import new_request

def home(request):
    form = NameForm(request.POST or None)
    if request.method == 'POST':
        print('posted')
        form = NameForm(request.POST)
        if form.is_valid():
            print('form valid')
            username = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            departments = form.cleaned_data.get('departments')
            all_category_choices = form.cleaned_data.get('all_category_choices')
            pws_project_url = form.cleaned_data.get('pws_project_url')
            subject = form.cleaned_data.get('subject')
            description = form.cleaned_data.get('description')
            all_priority = form.cleaned_data.get('all_priority')
            # messages.success(request, 'Ticket raised successfully',subject,description, extra_tags='alert')
            messages.success(request, ['Ticket raised successfully','subject : ',subject, 'description :', description, new_request(request)], extra_tags='alert')
            
            print(new_request(request))
            print(username, email, departments, all_category_choices, pws_project_url, subject, description, all_priority)
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


