from ci.pv.models import PV
from django.contrib import admin
from reversion.admin import VersionAdmin

class PVAdmin(VersionAdmin):
    pass
admin.site.register(PV, PVAdmin)

