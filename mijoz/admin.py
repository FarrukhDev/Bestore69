from django.contrib import admin
from mijoz.models import Mijoz

@admin.register(Mijoz)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("ism", "telefon","status")