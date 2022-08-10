from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
# Create your views here.
def register_user(request):
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("successful-signup")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

