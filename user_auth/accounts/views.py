from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from accounts.forms import UserSignUpForm

# Create your views here.

def index(request):
    """
        index page 
        
        Arguments:
            request (HttpRequest)
            
        Returns:
            In GET : render a page
        
    """
    return render(request,'accounts/index.html')

def signupview(request):
    """
        register user
        
        Arguments:
            request (HttpRequest)
        
        Required Parameter:
            username,password,email
        
        Returns:
            In Get: render a page
            In Post: save user details and register user
        
    """
    if request.method == 'POST':
        form= UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html',{'form':form})

@login_required
def dashboard(request):
    """
        show user details if user login successfully
        
        Arguments:
            request (HttpRequest)
        
        Returns:
            In Get: render a page
    """
    return render(request,'accounts/index.html')