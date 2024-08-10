from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('state_page', kwargs={'state_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class County(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='counties')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('county_page', kwargs={'state_slug': self.state.slug, 'county_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='cities')
    population = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_page', kwargs={
            'state_slug': self.county.state.slug, 
            'county_slug': self.county.slug, 
            'city_slug': self.slug
        })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
