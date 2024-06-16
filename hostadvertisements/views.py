from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from django.db.models import Q

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


from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from django.db.models import Q

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


class AdvertisementPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100  

class PublicAdvertisementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'city', 'country']
    ordering_fields = ['title', 'city', 'country']

    pagination_class = AdvertisementPagination

    def get_queryset(self):
        queryset = self.queryset
        title = self.request.query_params.get('title', None)
        city = self.request.query_params.get('city', None)
        country = self.request.query_params.get('country', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if country:
            queryset = queryset.filter(country__icontains=country)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def paginate_queryset(self, queryset):
        """
        Paginate the queryset and return a page if pagination is requested.
        """
        page_size = self.get_page_size(self.request)
        paginator = self.pagination_class()
        paginator.page_size = page_size

        if paginator.page_size:
            total_count = queryset.count()
            paginator.page.paginator._count = total_count
            paginator.page.paginator._per_page = page_size
            paginator.page.number = self.request.query_params.get(paginator.page_query_param, 1)
            paginator.page.paginator._num_pages = max(1, total_count // paginator.page.paginator.per_page)
        return paginator.paginate_queryset(queryset, self.request, view=self)