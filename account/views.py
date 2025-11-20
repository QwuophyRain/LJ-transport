from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from home.models import *
from driver.models import *
from . forms import *
from datetime import datetime



# Create your views here.
def index(request):
    return HttpResponse('users')

def register(request):
    setting = Settings.objects.get(pk=1)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}. Your account is created. You can check your account ')
            return redirect('/login2')
        else:
            messages.warning(request, form.errors)  # flash message
            return redirect('register')

    form = UserRegisterForm()
    context = {'form': form, 'setting': setting}
    return render(request, 'register.html', context)



def loginform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            messages.warning(request, 'Login Error!! Username or Password is Incorrect')
            return HttpResponseRedirect('/login')

    setting = Settings.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'login.html', context)



# def logoutfunc(request):
#     logout(request)
#     return HttpResponseRedirect('/')



def logout_request(request):
    messages.success(request,
                     f'You have succesfully logged out of your account.')

    logout(request)
    return HttpResponseRedirect('/')



@login_required(login_url='/login')   # shopping for only members
def profile(request):

    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)


    setting = Settings.objects.get(pk=1)
    current_user = request.user
    context = {'u_form': u_form, 'p_form': p_form, 'setting': setting}
    return render(request, 'profile.html', context)


@login_required(login_url='/login')   # shopping for only members
def profileUpdate(request):
    setting = Settings.objects.get(pk=1)
    current_user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated! You can check your account details under the ACCOUNT tab.')
            return redirect('/')
        else:
            messages.warning(request, p_form.errors)
            messages.warning(request, u_form.errors)
            return redirect('profile_update')
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)


    context = {'u_form': u_form, 'p_form': p_form, 'setting': setting,}
    return render(request, 'update_profile.html', context)



@login_required(login_url='/login')   # shopping for only members
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been update')
            return HttpResponseRedirect('/profile')
    else:
        setting = Settings.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        current_user = request.user


        context = {'setting': setting, 'user_form': user_form, 'profile_form': profile_form,}

        return render(request, 'update.html', context)



@login_required(login_url='/login')   # shopping for only members
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'You Password has been updated!')
            return HttpResponseRedirect('/profile')
        else:
            messages.error(request, 'Please correct the error below. <br>' + str(form-errors))
            return HttpResponseRedirect('account/password')
    else:
        setting = Settings.objects.get(pk=1)
        current_user = request.user
        form = PasswordChangeForm(request.user)

        return render(request, 'password_update.html', {'form': form, 'setting': setting,})