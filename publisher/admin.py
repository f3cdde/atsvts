from django.contrib import admin

from publisher import models

admin.site.register(models.UF)
admin.site.register(models.City)
admin.site.register(models.Newspaper)
admin.site.register(models.Font)
admin.site.register(models.NewspaperSection)
admin.site.register(models.PublicationTypeName)
admin.site.register(models.PublicationType)
admin.site.register(models.Client)
admin.site.register(models.Publication)
