
# urls.py
from django.urls import path
from .views import home, about, blog

urlpatterns = [
    path("", home, name="home" ),
    path("about-us/", about, name="about" ),
    path("blogs/", blog, name="blog" ),
]
