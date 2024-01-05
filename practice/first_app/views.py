from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def sing_up(request):
    if request.method == 'POST':
        sing_form = forms.RagistrationForm(request.POST)
        if sing_form.is_valid():
            sing_form.save()
            messages.success(request,'Account created Successfully')
            return redirect('user_login')
        
    else:
        sing_form = forms.RagistrationForm()
    return render(request, 'aut.html',{'form':sing_form, 'type' : 'Sing Up'} )

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request,'Logged In Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request,'Login information didnot matched')
                return redirect('sing_up')
            
    else:
        login_form = AuthenticationForm()
    return render(request,'aut.html',{'form':login_form, 'type':'login'})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('user_login')

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('user_login')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password.html', {'form' : form})


@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('user_login')
    
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'password.html', {'form' : form})