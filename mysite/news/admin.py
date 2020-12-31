from django.contrib import admin

from . import models

admin.site.register(models.Article)
admin.site.register(models.Reporter)
#增加对reporter的控制