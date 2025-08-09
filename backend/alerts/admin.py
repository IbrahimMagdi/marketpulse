from django.contrib import admin
from .models import *
admin.site.register(TriggeredAlert)
admin.site.register(Alert)
admin.site.register(Stock)

# Register your models here.
