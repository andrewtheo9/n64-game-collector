from django.contrib import admin
from .models import N64game, Session

# Register your models here.

admin.site.register(N64game)
admin.site.register(Session)