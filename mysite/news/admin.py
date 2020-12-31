from django.contrib import admin

from . import models

admin.site.register(models.Homework)
admin.site.register(models.Student)
#增加对reporter的控制,然后修改为student