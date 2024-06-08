from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import  AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import models
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'authentication_form.html', {'form' : register_form})

class UserLoginView(LoginView):
    template_name = 'authentication_form.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
@login_required
def profile(request):
    data = models.Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'data': data})

def update_profile(request):
    if request.method == 'POST':    
        profile_form = forms.ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserData(instance=request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})   
    