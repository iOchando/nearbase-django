from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Domain)
admin.site.register(DomainCredentials)
admin.site.register(Profile)
#admin.site.register(ProfileLibrary)
admin.site.register(PurchasedDomain)