from django.shortcuts import *
from . models import *
from . forms import *
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
@transaction.atomic
def RegisterView(request,pk=None):
    user_instance=get_object_or_404(User,id=pk) if pk else None
    profile_instance=get_object_or_404(Profile,user=user_instance) if user_instance else None
    if request.method=="POST":
        if pk:
            user_form=UserUpdateForm(request.POST,instance=user_instance)
        else:
            user_form=UserRegistrationForm(request.POST)
        profile_form=ProfileRegistrationForm(request.POST,request.FILES,instance=profile_instance)
        if user_form.is_valid() and profile_form.is_valid():
           user=user_form.save()
           profile=profile_form.save(commit=False)
           profile.user=user
           profile.save()
           if pk:
                messages.success(request,"Your profile has been updated successfully.")
           else:
                login(request, user)
                messages.success(request,f"Welcome {user.username}, your profile has been created.")
                return redirect("Note:dashboard")  
    else:
        if pk:
            user_form=UserUpdateForm(instance=user_instance)
        else:
           user_form=UserRegistrationForm()
        profile_form=ProfileRegistrationForm(instance=profile_instance)
        
    context={
            'u_f':user_form,
            'p_f':profile_form,
            'instance':user_instance
        }
    return render(request,"Register.html",context)
    
def LoginView(request):
    if request.user.is_authenticated:
        return redirect("Note:dashboard")
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,f"welcom Back, {user.username}")
            return redirect("Note:dashboard")
        else:
            messages.error(request,"Invalid Username and Password")
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{'form':form})
@login_required
def LogoutView(request):
    logout(request)
    messages.success(request,"You've been Sign Out")
    return redirect("Profile:loginu")