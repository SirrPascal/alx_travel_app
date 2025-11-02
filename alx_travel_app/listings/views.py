from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Listing, Category, Review
from django.shortcuts import render, get_object_or_404

# API Views
@swagger_auto_schema(
    method='get',
    operation_description="Get all travel listings",
    responses={200: openapi.Response('Successful response', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
            'listings': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_OBJECT))
        }
    ))}
)
@api_view(['GET'])
def get_listings(request):
    """
    Get all travel listings
    """
    listings = Listing.objects.all()
    listings_data = [{
        'id': listing.id,
        'title': listing.title,
        'location': listing.location,
        'price': str(listing.price),
        'status': listing.status,
        'category': listing.category.name
    } for listing in listings]
    
    return Response({
        'message': 'Travel listings retrieved successfully',
        'listings': listings_data
    }, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='post',
    operation_description="Create a new travel listing",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['title', 'location', 'price', 'category'],
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the listing'),
            'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the listing'),
            'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Price per person'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Detailed description'),
            'category': openapi.Schema(type=openapi.TYPE_INTEGER, description='Category ID'),
            'status': openapi.Schema(type=openapi.TYPE_STRING, description='Listing status')
        }
    ),
    responses={201: openapi.Response('Listing created successfully', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
            'listing_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of created listing')
        }
    ))}
)
@api_view(['POST'])
def create_listing(request):
    """
    Create a new travel listing
    """
    data = request.data
    try:
        category = Category.objects.get(id=data.get('category'))
        listing = Listing.objects.create(
            title=data.get('title'),
            description=data.get('description', ''),
            location=data.get('location'),
            price=data.get('price'),
            category=category,
            status=data.get('status', 'active')
        )
        return Response({
            'message': 'Travel listing created successfully',
            'listing_id': listing.id
        }, status=status.HTTP_201_CREATED)
    except Category.DoesNotExist:
        return Response({
            'error': 'Category not found'
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'error': str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

# Template Views
def listing_list(request):
    """View for displaying all listings"""
    listings = Listing.objects.all()
    categories = Category.objects.all()
    return render(request, 'listings/listing_list.html', {
        'listings': listings,
        'categories': categories
    })

def listing_detail(request, listing_id):
    """View for displaying a single listing"""
    listing = get_object_or_404(Listing, id=listing_id)
    reviews = listing.reviews.all()
    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'reviews': reviews
    })
