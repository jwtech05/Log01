from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profiles/profile.html')

@login_required
def profile_edit(request):
    return render(request, 'profiles/profile_update.html')