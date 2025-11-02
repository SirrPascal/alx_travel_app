from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('listings/', views.get_listings, name='get_listings'),
    path('listings/create/', views.create_listing, name='create_listing'),
    
    # Template views
    path('', views.listing_list, name='listing_list'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
]