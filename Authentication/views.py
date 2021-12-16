from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = ""
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                return redirect('/')
            else:
                message = "Invalid User"
        else:
            message = "Please fill up the forms"
        return render(request, 'Authentication/Login.html', {"message": message})

    return render(request, 'Authentication/Login.html')


def signup(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        print(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = ""
        if username and password and email:
            if User.objects.filter(email=email):
                message = "Email has already been registered!"
                return render(request, 'Authentication/Signup.html', {"message": message})
            if User.objects.filter(username=username):
                message = "Username has already been registered!"
                return render(request, 'Authentication/Signup.html', {"message": message})

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            return redirect('/login')
        else:
            message = "Please fill up the forms"
            return render(request, 'Authentication/Signup.html', {"message": message})

    return render(request, 'Authentication/Signup.html')


def logout(request):
    request.session['is_login'] = False
    return redirect('/')
