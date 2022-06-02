from django.contrib import admin
from .models import Order,District,Branch,Chocolate
# Register your models here.
admin.site.register(Order)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Chocolate)