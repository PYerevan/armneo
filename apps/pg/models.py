from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=32)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    capital = models.ForeignKey('Town', related_name='regions', on_delete=models.CASCADE, null=True,
                                blank=True)
    neighbour = models.ManyToManyField(to='self', related_name='neighbours', symmetrical=True)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=32)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=32)
    district = models.ForeignKey(District, related_name='towns', on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=32)
    district = models.ForeignKey(District, related_name='villages', on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name
