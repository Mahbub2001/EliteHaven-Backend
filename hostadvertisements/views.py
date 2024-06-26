from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class AdvertisementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication] 

    queryset = Advertisement.objects.all()  
    serializer_class = AdvertisementSerializer 

    def create(self, request, *args, **kwargs):
        try:
            print(request.data)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            print(e) 
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True) 
        self.perform_update(serializer)  
        return Response(serializer.data) 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()  
        self.perform_destroy(instance)  
        return Response(status=status.HTTP_204_NO_CONTENT) 


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        total_count = self.page.paginator.count
        page_size = self.get_page_size(self.request)

        return Response({
            'total_count': total_count,
            'num_pages': (total_count + page_size - 1) // page_size,
            'results': data
        })

class PublicAdvertisementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'city', 'country']
    ordering_fields = ['title', 'city', 'country']

    pagination_class = CustomPagination  

    def get_queryset(self):
        queryset = Advertisement.objects.all().order_by('-id') 
        title = self.request.query_params.get('title', None)
        city = self.request.query_params.get('city', None)
        country = self.request.query_params.get('country', None)
        host_id = self.request.query_params.get('host_id', None)  

        if title:
            queryset = queryset.filter(title__icontains=title)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if country:
            queryset = queryset.filter(country__icontains=country)
        if host_id:
            queryset = queryset.filter(host=host_id)

        return queryset