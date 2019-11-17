from django.contrib import admin
from . import models

admin.site.register(models.candidate)
admin.site.register(models.eligible)
admin.site.register(models.company)
admin.site.register(models.poc)
admin.site.register(models.announcement)
