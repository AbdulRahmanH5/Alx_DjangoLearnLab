from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('home')
        
        else:
            form = UserCreationForm
            
        return render(request, 'registration/register.html', {'form': form})
    
@login_required
def profile_view(requets):
    return render(requets, 'registration/profile.html')