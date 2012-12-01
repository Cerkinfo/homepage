from models import Fortune
from django.contrib import admin
from reversion.admin import VersionAdmin

class FortuneAdmin(VersionAdmin):
    pass
admin.site.register(Fortune, FortuneAdmin)

