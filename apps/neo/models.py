from py2neo import Graph
from py2neo.ogm import GraphObject, Property, RelatedTo
from django.conf import settings

# Create your models here.
graph = Graph(
    host=settings.NEO4J_HOST,
    port=settings.NEO4J_PORT,
    user=settings.NEO4J_USER,
    password=settings.NEO4J_PASSWORD,
)


class BaseModel(GraphObject):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def all(self):
        return self.match(graph)

    def save(self):
        graph.push(self)

    def delete(self):
        graph.delete(self)


class Country(BaseModel):
    __primarykey__ = 'name'

    name = Property()


class Region(BaseModel):
    __primarykey__ = 'name'

    name = Property()
    population = Property()

    country = RelatedTo('Country', 'BELONGS_TO')


class District(BaseModel):
    __primarykey__ = 'name'

    name = Property()
    population = Property()

    region = RelatedTo('Region', 'BELONGS_TO')


class City(BaseModel):
    __primarykey__ = 'name'

    name = Property()
    population = Property()

    region = RelatedTo('Region', 'IS_CAPITAL_OF')

    district = RelatedTo('District', 'BELONGS_TO')


class Village(BaseModel):
    __primarykey__ = 'name'

    name = Property()
    population = Property()

    district = RelatedTo('District', 'BELONGS_TO')
