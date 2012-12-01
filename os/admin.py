from ci.os.models import OS
from django.contrib import admin
from reversion.admin import VersionAdmin

class OSAdmin(VersionAdmin):
    pass

admin.site.register(OS, OSAdmin)

