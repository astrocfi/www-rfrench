from django.contrib import admin
from .models import Gig
from .models import Event

# Register your models here.
admin.site.register(Gig)
admin.site.register(Event)
