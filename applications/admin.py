from django.contrib import admin
from .models import GeneralInfo, HeroCarousel, ViewMore, Author, Blog, Gallery, UpcomingEvent
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Register your models here.
# admin.site.register(User)

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ["director",  "company_logo", 'email' ]

@admin.register(HeroCarousel)
class HeroCarouselAdmin(admin.ModelAdmin):
    list_display = ["theme",  "description" ]

@admin.register(ViewMore)
class ViewMoreAdmin(admin.ModelAdmin):
    list_display = ["theme"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name"]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(Gallery)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["event_name"]

@admin.register(UpcomingEvent)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title"]
