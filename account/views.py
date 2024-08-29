# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .forms import UserRegistrationForm
# from django.contrib.auth.views import LoginView

# # write sign-up views 
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             # messages.success("Account Successfully Created")
#             return redirect('/login')
#     else:
#         form = UserRegistrationForm()
#         # messages
#     return render(request, 'registration/register.html', {'form':form})


# class CustomLoginView(LoginView):
#     template_name ='registration/login.html'    
    

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
    template_name = 'registration/login.html'
    form_class = CustomLoginForm
    success_url = reverse_lazy('home')

