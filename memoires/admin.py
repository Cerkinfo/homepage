from ci.memoires.models import Memoire
from django.contrib import admin
from reversion.admin import VersionAdmin

class MemoireAdmin(VersionAdmin):
    pass
admin.site.register(Memoire, MemoireAdmin)
