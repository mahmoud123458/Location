from django.contrib import admin
from .models import Country, State, County, City

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CountyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(City, CityAdmin)
