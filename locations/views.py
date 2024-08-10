from django.shortcuts import render, get_object_or_404
from .models import Country, State, County, City

def country_page(request):
    country = Country.objects.first()  # Assuming you only have one country
    states = State.objects.all()

    # Prepare data for each state including top 3 cities
    state_city_data = []
    for state in states:
        top_cities = City.objects.filter(county__state=state).order_by('-population')[:3]
        state_city_data.append({
            'state': state,
            'top_cities': top_cities
        })

    context = {
        'country': country,
        'state_city_data': state_city_data,
    }
    return render(request, 'locations/country_page.html', context)

def state_page(request, state_slug):
    state = get_object_or_404(State, slug=state_slug)
    counties = state.counties.all()

    # Prepare data for each county including top 3 cities
    county_city_data = []
    for county in counties:
        top_cities = county.cities.order_by('-population')[:3]
        county_city_data.append({
            'county': county,
            'top_cities': top_cities
        })

    context = {
        'state': state,
        'county_city_data': county_city_data,
    }
    return render(request, 'locations/state_page.html', context)


def county_page(request, state_slug, county_slug):
    state = get_object_or_404(State, slug=state_slug)
    county = get_object_or_404(County, slug=county_slug, state=state)
    cities = county.cities.all()
    context = {
        'state': state,
        'county': county,
        'cities': cities,
    }
    return render(request, 'locations/county_page.html', context)

def city_page(request, state_slug, county_slug, city_slug):
    state = get_object_or_404(State, slug=state_slug)
    county = get_object_or_404(County, slug=county_slug, state=state)
    city = get_object_or_404(City, slug=city_slug, county=county)
    context = {
        'state': state,
        'county': county,
        'city': city,
    }
    return render(request, 'locations/city_page.html', context)
