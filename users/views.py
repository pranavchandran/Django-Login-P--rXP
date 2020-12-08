from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from users.forms import RegisterForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            import pdb;pdb.set_trace()
    return render (request, 'users/register.html', {'form': form})


