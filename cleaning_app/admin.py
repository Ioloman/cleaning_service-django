from django.contrib import admin
from .models import Service, ServiceType, UserService

# Register your models here.
admin.site.register(ServiceType)
admin.site.register(Service)
admin.site.register(UserService)
