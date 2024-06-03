from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')

def signupview(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

@login_required
def dashboard(request):
    print(request.user.pk)
    return render(request,'accounts/index.html')