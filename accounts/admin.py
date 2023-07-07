from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.admin import SiteAdmin
from django.contrib.sites.models import Site

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, CustomSite


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # list_display = ['email', 'username',]

class CustomSiteAdmin(SiteAdmin):
    # Override default properties and methods as needed
    # pass
    list_display = ['custom_id', 'domain', 'name', 'meta_description']
    
    def custom_id(self, obj):
        return obj.id

    custom_id.short_description = 'SITE_ID'  # Change the column header label


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Site) #original SITES panel
admin.site.register(CustomSite, CustomSiteAdmin)