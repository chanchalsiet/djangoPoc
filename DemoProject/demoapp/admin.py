from demoapp.models import Menu
from django.contrib import admin

from .models import Logger
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith",)


# Register your models here.
admin.site.register(Logger)
admin.site.register(Menu)
