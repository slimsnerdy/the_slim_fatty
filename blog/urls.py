from .views import PostList, PostDetail, SearchView
from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    path('disclaimer/', TemplateView.as_view(template_name = 'disclaimer.html'), name = 'disclaimer'),
    path('privacy/', TemplateView.as_view(template_name = 'privacy.html'), name = 'privacy'),
    path('search/', SearchView.as_view(), name = 'search'),
    # path('search/', views.search, name = 'search'),     #function based view
    path('<slug:slug>/', PostDetail.as_view(), name = 'post_detail'),
    path('', PostList.as_view(), name = 'home'),
]