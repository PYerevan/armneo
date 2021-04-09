from apps.pg.models import Town, Village, District, Region
import pandas as pd


def load_cities_and_villages(path):
    data = pd.read_csv(path)
    for index, place in data.iterrows():
        try:
            district = District.objects.get(name=place['district'])
        except District.DoesNotExist:
            raise ValueError(f"District with name {place['district']} doesn't exit. Index {index}")

        if place['type'] == 'Village':
            Village.objects.update_or_create(name=place['name'], district=district, population=place['population'])
        elif place['type'] in ['Town', 'City']:
            Town.objects.update_or_create(name=place['name'], district=district, population=place['population'])


def load_districts(path):
    data = pd.read_csv(path)
    for index, district in data.iterrows():
        try:
            region = Region.objects.get(name=district['region'])
        except Region.DoesNotExist:
            raise ValueError(f"Region with name {district['region']} doesn't exit. Index {index}")

        District.objects.update_or_create(name=district['name'], region=region, population=district['population'])
