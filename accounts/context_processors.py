from .models import CustomSite

def custom_site(request):
    site = CustomSite.objects.first()  # Assuming there's at least one CustomSite instance
    # site = CustomSite.objects.get(id=5)  # change the site
    # site = CustomSite.objects.get(id=1)  # change the site
    return {'site': site}