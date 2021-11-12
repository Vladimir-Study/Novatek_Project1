from django.contrib import admin
from .models import *


class StationAdmin(admin.ModelAdmin):
    list_display = ('station_number',)


class EngineAdmin(admin.ModelAdmin):
    list_display = ('engine_number',)

class ParametersAdmin(admin.ModelAdmin):
    list_display = ('station', 'engine', 'time_work', 'volume_oil',)    


admin.site.register(Engine, EngineAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(EnergyGenerate)
admin.site.register(gas_par)
admin.site.register(DateCheck)
admin.site.register(Parameters, ParametersAdmin)