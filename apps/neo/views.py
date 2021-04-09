from django.shortcuts import render

# Create your views here.


from apps.pg.models import Region

Region.objects.select_related()