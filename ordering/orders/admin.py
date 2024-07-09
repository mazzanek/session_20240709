from django.contrib import admin
from .models import order


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "address")


admin.site.register(order, OrderAdmin)