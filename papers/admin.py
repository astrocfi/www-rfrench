from django.contrib import admin
from .models import PaperCategory, PaperSubCategory, Paper

admin.site.register(PaperCategory)
admin.site.register(PaperSubCategory)
admin.site.register(Paper)
