from django.contrib import admin
from other.models import Reklama, Blog, MySettings, Team
# Register your models here.

admin.site.register(Reklama)
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(MySettings)