from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserCreationForm

def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'account/profile.html', {'user':user})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('OK')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup_form.html', {'form':form})
