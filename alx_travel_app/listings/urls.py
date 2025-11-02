from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.get_listings, name='get_listings'),
    path('listings/create/', views.create_listing, name='create_listing'),
]