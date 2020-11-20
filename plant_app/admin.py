from django.contrib import admin

# Register your models here.
from .models import Plant
from .models import Water
admin.site.register(Plant)

admin.site.register(Water)
