from django.shortcuts import render
from .models import GeneralInfo, HeroCarousel, ViewMore, Blog, Gallery, UpcomingEvent
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    general_info = GeneralInfo.objects.first()
    hero_images = HeroCarousel.objects.all()
    # view_images = HeroCarousel.objects.all().order_by('-created_at')[:3]
    events = Gallery.objects.all()[:3]
    blogs = Blog.objects.all()[:3]
    view_images = ViewMore.objects.first()
    main_shows = UpcomingEvent.objects.all()[:1]


    context = {
        
        "company_logo": getattr(general_info, "company_logo", ""),

        "hero_images":hero_images,

        # 'view_image':view_images.bg_image,
        "view_image": getattr(view_images, "bg_image", ""),
        "blogs":blogs,
        "events":events,
        # "image_show": main_shows.image.url if main_shows.image else None,
        # "title_show": main_shows.title,
        "main_shows": main_shows,

    }
    return render(request, "index.html", context)
    

# Create your views here.
@login_required(login_url='/login')
def about(request):
    context = {} 
    return render(request, "about.html", {})

# Create your views here.
@login_required(login_url='/login')
def blog(request):
    context = {} 
    return render(request, "blog.html", {})

@login_required(login_url='/login')
def designersApp(request):
    context = {} 
    return render(request, "designers-application.html", {})


