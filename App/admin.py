from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Employee)
admin.site.register(ProductData)
admin.site.register(Product)