
# urls.py
from django.urls import path
from .views import home, about, blog, designersApp

urlpatterns = [
    path("", home, name="home" ),
    path("about-us/", about, name="about" ),
    path("blogs/", blog, name="blog" ),
    path("designers-apply/", designersApp, name="designers-application" ),
]
