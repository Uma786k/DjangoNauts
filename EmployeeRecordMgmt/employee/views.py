from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def index(reqest):
    return render(reqest,'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # replace 'home' with the name of your home page URL pattern
        else:
            error_message = "Invalid login credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
