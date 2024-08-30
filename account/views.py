from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, CustomLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Sign-up view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('home')  # Redirect to the home page after login

