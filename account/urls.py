from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView
from applications.views import home


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', home, name='home'),
]

