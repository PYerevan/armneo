from django.contrib import admin

# Register your models here.
from apps.pg.models import Region, Country, District, Town, Village

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Town)
admin.site.register(Village)
