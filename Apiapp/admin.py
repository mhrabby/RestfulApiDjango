from django.contrib import admin

from .models import *

admin.site.register(Employees)
admin.site.register(Authority)
admin.site.register(Buyer)

