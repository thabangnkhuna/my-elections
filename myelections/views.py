from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Member

def login(request):
    return LoginView.as_view(template_name='login.html')(request)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can log the user in immediately after signing up
            # by using Django's authentication login() function.
            # Refer to Django documentation for more details.
            return redirect('login')  # Redirect to the login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def member_dashboard(request):
    print(request.user)  # Add this line to check if the user is authenticated
    return render(request, 'member_dashboard.html')

@login_required
def logout(request):
    # Your logout logic here
    return render(request, 'logged_out.html')

def home(request):
    return render(request, 'home.html')

def members(request):
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})

def about(request):
    return render(request, 'about.html')
