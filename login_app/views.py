
from django import forms
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from login_app.models import CreateUser
from .forms import CreateFrom


# Create your views here.
def index(request):
    return render(request, 'login_app/home.html')


def reg_user(request):
    if request.method == 'POST':
        frm = CreateFrom(request.POST, request.FILES)
        if frm.is_valid():
            full_name = frm.changed_data.get('full_name')
            image = frm.cleaned_data.get('image')
            user_name = frm.cleaned_data.get('user_name')
            email = frm.cleaned_data.get('email')
            password1 = frm.cleaned_data.get('password1')
            password2 = frm.cleaned_data.get('password2')

            if User.objects.filter(user_name=user_name).exists():
                messages.error(request, 'Sorry {0} is already exists'.format(user_name))
                return redirect('login_app:signup')
            else:
                if password1 != password2:
                    messages.error(request, "Oops! password doesn't match!")
                    return redirect('login_app:signup')
                else:
                    password_hash = make_password(password2)
                    user = User.objects.create(
                        user_name=user_name, password=password_hash, email=email
                    )

                    new_user = user
                    new_user.full_name = full_name
                    new_user.image = image
                    new_user.save()
                    messages.success(
                        request, 'Congratulations {0} your account has been craated successfully'.format(user)
                        )
    else:
        frm= CreateFrom()
    return render(request, 'login_app/signUp.html', {'form':frm})




