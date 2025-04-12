from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # تغيير إلى الصفحة المناسبة بعد التسجيل
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # تغيير إلى الصفحة المناسبة بعد تسجيل الدخول
    else:
        form = CustomAuthenticationForm()
    return render(request, 'core/login.html', {'form': form})
