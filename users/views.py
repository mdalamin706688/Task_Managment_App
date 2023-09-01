from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, CustomUserCreationForm,  CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Check if a UserProfile already exists for the user, create one if not
            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user)
            
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user  # Get the current user

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Update the user's information
            profile_form.save()  # Update the user's profile information
            update_session_auth_hash(request, user_form.instance)  # Update the session's authentication hash to prevent logouts
            messages.success(request, 'Your profile has been updated!')
            return redirect('task_list')
    else:
        user_form = CustomUserChangeForm(instance=user)
        profile_form = UserProfileForm(instance=user.userprofile)

    return render(
        request,
        'registration/edit_profile.html',
        {'user_form': user_form, 'profile_form': profile_form}
    )

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
