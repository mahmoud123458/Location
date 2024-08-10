from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_page, name='country_page'),
    path('<slug:state_slug>/', views.state_page, name='state_page'),
    path('<slug:state_slug>/<slug:county_slug>/', views.county_page, name='county_page'),
    path('<slug:state_slug>/<slug:county_slug>/<slug:city_slug>/', views.city_page, name='city_page'),
]
