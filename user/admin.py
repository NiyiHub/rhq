from django.contrib import admin
from .models import RHQUser


class RHQUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'username')


admin.site.register(RHQUser, RHQUserAdmin)
