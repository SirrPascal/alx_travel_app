from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    operation_description="Get all travel listings",
    responses={200: openapi.Response('Successful response', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
            'listings': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
        }
    ))}
)
@api_view(['GET'])
def get_listings(request):
    """
    Get all travel listings
    """
    return Response({
        'message': 'Travel listings retrieved successfully',
        'listings': [
            {'id': 1, 'title': 'Paris Adventure', 'location': 'Paris, France'},
            {'id': 2, 'title': 'Tokyo Experience', 'location': 'Tokyo, Japan'}
        ]
    }, status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='post',
    operation_description="Create a new travel listing",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['title', 'location', 'price'],
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the listing'),
            'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the listing'),
            'price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Price per person'),
            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Detailed description')
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
    return Response({
        'message': 'Travel listing created successfully',
        'listing_id': 123
    }, status=status.HTTP_201_CREATED)
