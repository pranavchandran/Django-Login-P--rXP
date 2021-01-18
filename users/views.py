from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from .forms import ContractForm
from django.contrib import messages
from django.db.models import Q
# Create your views here.
import time
from .requesting import new_request
from .models import Status

def home(request):
    form = ContractForm(request.POST or None)
    if request.method == 'POST':
        print('posted')
        form = ContractForm(request.POST)
        print(form)
        if form.is_valid():
            
            # print('form valid')
            # username = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # departments = form.cleaned_data.get('departments')
            form.save()
            # all_category_choices = form.cleaned_data.get('all_category_choices')
            # pws_project_url = form.cleaned_data.get('pws_project_url')
            # subject = form.cleaned_data.get('subject')
            # description = form.cleaned_data.get('description')
            # all_priority = form.cleaned_data.get('all_priority')
            # all_ticket_status = form.cleaned_data.get('all_ticket_status')
            # time_tuple = time.localtime() # get struct_time
            # time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)

            # messages.success(request, 'Ticket raised successfully',subject,description, extra_tags='alert')
            print(username, all_ticket_status)
            messages.success(request, ['Ticket raised successfully','subject : ',subject, 'description :', description, new_request(request), time_string], extra_tags='alert')
            user_id_1 = Status.objects.all()
            for login_user in user_id_1:
                if str(login_user.user) == username:
                    print('Login user matched')
                if login_user.status != all_ticket_status:
                    form.all_ticket_status = login_user.status

                    form.save()

            
                
                    # import pdb; pdb.Pdb(skip=['django.*']).set_trace()
            # user_id_1 = Q(Status__startswith=username)
            # print(user_id_1.check_status,user_id_1.user)  
            print(user_id_1)

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


