from django.contrib import admin
from .models import *


admin.site.register(Manager)
admin.site.register(Client)
admin.site.register(Apartment)
admin.site.register(Review)