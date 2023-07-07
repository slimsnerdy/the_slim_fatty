from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# from .models import CustomSite
# from django.views.generic import TemplateView

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# class MyView(TemplateView):
#     template_name = 'base.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         site = CustomSite.objects.get_current()
#         context['site_meta_description'] = site.site_meta_description
#         return context