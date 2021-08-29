from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account-login')
    else:
        form = CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'clownApp/account/register.html', context)


def profile(request):
    context = {
        # 'form': form
    }
    return render(request, 'clownApp/account/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account-profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'clownApp/account/profile_update.html', context)


def login(request):
    context = {
        # 'form': form
    }
    return render(request, 'clownApp/account/login.html', context)


def logout(request):
    context = {
        # 'form': form
    }
    return render(request, 'clownApp/account/logout.html', context)
