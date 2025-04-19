from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileUpdateForm
from .models import Course, Lesson, Enrollment, User, Category, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

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

# profile page
@login_required
def profile_view(request):
    if request.user.is_authenticated:
        user = request.user
        enrollments = Enrollment.objects.filter(user=user)
        return render(request, 'core/profile.html', {'user': user, 'enrollments': enrollments})
    else:
        return redirect('login')  # تغيير إلى صفحة تسجيل الدخول إذا لم يكن المستخدم مسجلاً الدخول

# home page
def home_view(request):
    courses = Course.objects.all()
    return render(request, 'core/home.html', {'courses': courses})

# courses page
def courses_view(request):
    courses = Course.objects.all()
    return render(request, 'core/courses.html', {'courses': courses})

@login_required
def update_profile(request):
    if request.method == 'POST':
        # تحديث البيانات الأساسية فقط
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        
        # التحقق من صحة البيانات
        if not username or not email:
            messages.error(request, 'يرجى ملء جميع الحقول المطلوبة')
            return redirect('update_profile')
        
        # التحقق من عدم تكرار اسم المستخدم
        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            messages.error(request, 'اسم المستخدم مستخدم بالفعل')
            return redirect('update_profile')
        
        # التحقق من عدم تكرار البريد الإلكتروني
        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            messages.error(request, 'البريد الإلكتروني مستخدم بالفعل')
            return redirect('update_profile')
        
        # تحديث بيانات المستخدم
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()
        
        # تحديث الملف الشخصي
        # التحقق من وجود ملف شخصي للمستخدم
        try:
            # البحث عن ملف شخصي مرتبط بالمستخدم
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            # إنشاء ملف شخصي جديد إذا لم يكن موجودًا
            profile = Profile(user=user)
        
        profile.bio = bio
        
        # تحديث الصورة الشخصية إذا تم تحميلها
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        
        profile.save()
        
        # تحديث العلاقة بين المستخدم والملف الشخصي
        user.Profile = profile
        user.save()
        
        messages.success(request, 'تم تحديث الملف الشخصي بنجاح')
        return redirect('profile')
    
    return render(request, 'core/update_profile.html')