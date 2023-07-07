"""the_slim_fatty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#robots.txt simemap.xml CODE
from django.views.generic.base import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Post
info_dict = {
    # 'queryset': Post.objects.all(),
    'queryset': Post.objects.filter(status=1),  #NO DRAFTS INCLUDED
}

from environs import Env

env = Env()
env.read_env()

urlpatterns = [ #PRODUCTION/LIVE
    path(env.str('BOSSY'), admin.site.urls), #HIDDEN 🎀
    path('accounts/', include('accounts.urls')),  # new
    path('accounts/', include ('django.contrib.auth.urls')),
    path('', include('contact.urls')), # new
    path('', include('blog.urls')),
    path('captcha/', include('captcha.urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path(
        'sitemap.xml', sitemap,
        # {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6, protocol='https')}},
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        #ONLY FOR LOCAL/DEBUG MODE

# if settings.DEBUG:
#     # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),    #DEBUG TRUE LOCALHOST
        path('accounts/', include('accounts.urls')),  # new
        path('accounts/', include ('django.contrib.auth.urls')),
        path('', include('contact.urls')), # new
        path('', include('blog.urls')),
        path('captcha/', include('captcha.urls')),
        path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
        path(
            'sitemap.xml', sitemap,
            # {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6, protocol='https')}},
            {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
            name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'the_slim_fatty.views.custom_404'