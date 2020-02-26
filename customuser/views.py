from django.shortcuts import render, redirect
from django.contrib import messages


from django.contrib.auth import login, authenticate, logout

# Create your views here.
from .forms import LoginForm, RegistrationFrom


def register_user(request):

    form = RegistrationFrom()

    if request.method == 'POST':
        form = RegistrationFrom(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
    
    return render(request, 'customuser/register.html', { 'form': form })


def login_user(request):
    """ view for login """

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                if user.user_type=="Plaintiff":
                    return redirect('user_home')
                elif user.user_type=="Lawyer":
                    return redirect('lawyer_home')
                elif user.user_type=="Witness":
                    return redirect('witness_home')

                return redirect('home')
            else:
                messages.add_message(request, messages.INFO, 'Invalid username or password')



    return render(request,'customuser/login.html', { 'form' : form })


def logout_user(request):
    logout(request)
    return redirect('login')