from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})



def register_view(request):
    # Handle POST request when the form is submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Populate form with submitted data
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Automatically log in the newly registered user
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the home page
        else:
            # Display form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserCreationForm()  # Initialize an empty form for GET request

    # Render the registration form template
    return render(request, 'registration/register.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'registration/profile.html')



@login_required
def about(request):
    return render(request, 'registration/about.html')



@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('login')  # Or redirect to home or login page after logout

    # For GET: show the confirmation page
    return render(request, 'registration/logout.html')