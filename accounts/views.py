from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ResetPasswordForm
from .forms import ChangeUsernameForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm
from django.contrib.auth.hashers import check_password

# Create your views here.

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {'title': 'Login'}
    if request.method == 'GET':
        return render(request, 'accounts/login.html', {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html', {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')

from django.contrib.auth.hashers import make_password

def signup(request):
    template_data = {'title': 'Sign Up'}
    
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save(commit=False)  # Save without committing to modify fields
            
            # Correct field names
            user.securityQ1 = form.cleaned_data['security_question_1']
            user.securityQ2 = form.cleaned_data['security_question_2']
            user.securityA1 = make_password(form.cleaned_data['security_answer_1']) 
            user.securityA2 = make_password(form.cleaned_data['security_answer_2'])

            user.save()  # Save user after setting fields
            return redirect('accounts.login')
        
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})

def resetpassword(request):
    template_data = {'title': 'Reset Password'}

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_answers = {
                form.cleaned_data['security_question_1']: form.cleaned_data['security_answer_1'],
                form.cleaned_data['security_question_2']: form.cleaned_data['security_answer_2']
            }

            # Use get_user_model() instead of directly importing User
            User = get_user_model()
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                template_data['error'] = "Username not found."
                template_data['form'] = form
                return render(request, 'accounts/resetpassword.html', template_data)

            stored_answers = {
                user.securityQ1: user.securityA1,
                user.securityQ2: user.securityA2
            }

            # Check if user-provided answers match the stored answers (regardless of order)
            match_count = sum(
                check_password(user_answers[q], stored_answers[q]) for q in user_answers if q in stored_answers
            )

            if match_count == 2:  # Both answers must match
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                return redirect('accounts.login')
            else:
                template_data['error'] = "Incorrect security question answers."

    else:
        form = ResetPasswordForm()

    template_data['form'] = form
    return render(request, 'accounts/resetpassword.html', template_data)

@login_required
def change_username(request):
    messages.get_messages(request).used = True

    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']

            # Update the current user's username
            request.user.username = new_username
            request.user.save()
            messages.success(request, "Your username has been updated successfully!")
            return redirect('home.index')
    else:
        form = ChangeUsernameForm()

    return render(request, 'accounts/change_username.html', {'form': form})

@login_required
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            request.user.set_password(form.cleaned_data["new_password"])
            request.user.save()
            update_session_auth_hash(request, request.user)  # Prevents logout after password change
            messages.success(request, "Your password has been changed successfully.")
            return redirect("home.index")
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, "accounts/change_password.html", {"form": form})

@login_required
def account(request):
    if request.method == "POST":
        if 'change_username' in request.POST:
            username_form = ChangeUsernameForm(request.POST)
            password_form = CustomPasswordChangeForm(request.user)

            if username_form.is_valid():
                new_username = username_form.cleaned_data['new_username']
                request.user.username = new_username
                request.user.save()
                messages.success(request, "Your username has been updated successfully!")
                return redirect('account')

        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            username_form = ChangeUsernameForm()

            if password_form.is_valid():
                request.user.set_password(password_form.cleaned_data["new_password"])
                request.user.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, "Your password has been changed successfully.")
                return redirect('account')
    else:
        username_form = ChangeUsernameForm()
        password_form = CustomPasswordChangeForm(request.user)

    context = {
        'username_form': username_form,
        'password_form': password_form
    }
    return render(request, 'accounts/account.html', context)