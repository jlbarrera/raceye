from django.contrib import admin

from .models import RacesWebsite
from .models import Race

admin.site.register(RacesWebsite)
admin.site.register(Race)