from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserSignUpForm(UserCreationForm):
    """ User Register form 

        extends:
            UserCreationForm
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def clean_password1(self):
        password = self.cleaned_data['password1']
        if len(password)<8:
            self.add_error("password1","password must be 8 characters long")
        return password

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            self.add_error("password2","Password does not match")
        return password2