from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UpdateUserForm, LoginForm, EmailVerifacationForm
from .models import CustomUser
from django.core.mail import send_mail
from .models import Code
from ecommerce.settings import EMAIL_HOST_USER
from django.http import HttpResponse

User = get_user_model()



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            username = request.POST.get('username')
            password = request.POST.get('password1')
            email = request.POST.get('email')

            user = authenticate(username=username, password=password, firstname=firstname, lastname=lastname)
            if user:
                user_code = Code.objects.create(user=user)
                user_code.genarate_code
                if user_code.number:
                    send_mail('Verification code', str(user_code.number), EMAIL_HOST_USER, [email, ])
                    return render(request, 'verify.html', {'id': user.id})
            return redirect('index')
    return render(request, 'register.html')


def resend_code(request, id):
    user = User.objects.get(id=id)
    user_code = Code.objects.get(user=user)
    user_code.genarate_code
    send_mail('Verification code', str(user_code.number), EMAIL_HOST_USER, [user.email])
    return render(request, 'verify.html', {'id': id})


def verify(request, id):
    if request.method == 'POST':
        form = EmailVerifacationForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=int(id))
            number = request.POST.get('code')
            own_code = Code.objects.get(user_id=user.id)
            print(number, own_code, number == own_code)
            if str(number) == str(own_code):
                login(request, user)
                user.is_verified = True
                user.save()
                return redirect('index')
            return HttpResponse("Error")



def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            return redirect('login')
    return render(request, 'login.html')


def profile(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')

        if not username:
            return redirect('profile')

        user = CustomUser.objects.get(id=request.user.id)

        if not user:
            return redirect('profile')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('index')
    return render(request, 'profile.html')


def change_password(request):
    if request.method == 'POST':
        user = request.user
        password_old = request.POST.get('password_old')
        password_new1 = request.POST.get('password_new1')
        password_new2 = request.POST.get('password_new2')

        if password_new2 != password_new1:
            return redirect('change_password')

        if not user.check_password(password_old):
            return redirect('change_password')

        user.set_password(password_new1)
        user.save()
        if user:
            login(request, user)
            return redirect('index')
        return redirect('index')
    return render(request, 'change_password.html')


def logout_view(request):
    logout(request)
    return redirect('index')
