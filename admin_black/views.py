from django.shortcuts import render, redirect
from admin_black.forms import RegistrationForm,LoginForm,UserPasswordResetForm,UserSetPasswordForm,UserPasswordChangeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def auth_signup(request):
  if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
        form.save()
        print('Account created successfully!')
        return redirect('/accounts/auth-signin/')
      else:
        print("Registration failed!")
  else:
    form = RegistrationForm()
  context = {'form': form}
  return render(request, 'accounts/auth-signup.html', context)

class AuthSignin(auth_views.LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/forgot-password.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/recover-password.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/recover-password.html'
  form_class = UserSetPasswordForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/auth-signin/')

# Pages -- Dashboard
def dashboard(request):
    context = {
    'parent': 'pages',
    'segment': 'dashboard'
  }
    return render(request, 'pages/dashboard.html', context)

@login_required(login_url='/accounts/auth-signin')
def icons(request):
    context = {
    'parent': 'pages',
    'segment': 'icons'
  }
    return render(request, 'pages/icons.html', context)

@login_required(login_url='/accounts/auth-signin')
def map(request):
    context = {
    'parent': 'pages',
    'segment': 'map'
  }
    return render(request, 'pages/map.html', context)

@login_required(login_url='/accounts/auth-signin')
def notifications(request):
    context = {
    'parent': 'pages',
    'segment': 'notifications'
  }
    return render(request, 'pages/notifications.html', context)

@login_required(login_url='/accounts/auth-signin')
def user_profile(request):
    context = {
    'parent': 'pages',
    'segment': 'user_profile'
  }
    return render(request, 'pages/user.html', context)

@login_required(login_url='/accounts/auth-signin')
def tables(request):
    context = {
    'parent': 'pages',
    'segment': 'tables'
  }
    return render(request, 'pages/tables.html', context)

@login_required(login_url='/accounts/auth-signin')
def typography(request):
    context = {
    'parent': 'pages',
    'segment': 'typography'
  }
    return render(request, 'pages/typography.html', context)

@login_required(login_url='/accounts/auth-signin')
def rtl(request):
    context = {
    'parent': 'pages',
    'segment': 'rtl'
  }
    return render(request, 'pages/rtl.html', context)
  
@login_required(login_url='/accounts/auth-signin')
def upgrade(request):
    context = {
    'parent': 'pages',
    'segment': 'upgrade'
  }
    return render(request, 'pages/upgrade.html', context)
