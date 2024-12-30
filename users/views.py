from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from carts.views import addCart_item
from .forms import UserLoginForm,UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
           
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



def login_view(request):
    if request.method =="POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password = password)
            if user is not None:

                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid username or password ')
        else:
            messages.error("there is samething wrong !")
    else:
        form = UserLoginForm()
    return render(request,'users/login.html',{'form':form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request,'users/home.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)