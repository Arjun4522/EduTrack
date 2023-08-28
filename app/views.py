from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)

        if user_form.is_valid():
            enrollment_number = user_form.cleaned_data['enrollment_number']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            phone_number = user_form.cleaned_data['phone_number']
            password = user_form.cleaned_data['password']
            confirm_password = user_form.cleaned_data['confirm_password']

            if password == confirm_password:
                if User.objects.filter(username=enrollment_number).exists():
                    user_form.add_error('enrollment_number', 'User with this enrollment number already exists')
                else:
                    user = User.objects.create_user(username=enrollment_number, password=password, email=email)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.email = email                   
                    user.phone_number = phone_number
                    user.save()

                    return render(request, 'registration_success.html')
            else:
                user_form.add_error('confirm_password', 'Passwords do not match')
    else:
        user_form = RegistrationForm()

    return render(request, 'registration.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        enrollment_number = request.POST.get('enrollment_number')
        password = request.POST.get('password')

        user = authenticate(username=enrollment_number, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'login_success.html')  
        else:
            error_message = "Invalid enrollment number or password"
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('index')

