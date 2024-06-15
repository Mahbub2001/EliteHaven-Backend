# views.py
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import HostRequest, Host
from .serializers import HostRequestSerializer, HostSerializer,AdminActionSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import Group

class HostRequestViewSet(viewsets.ModelViewSet):
    queryset = HostRequest.objects.all()
    serializer_class = HostRequestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['person'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AdminActionView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = AdminActionSerializer(data=request.data)
        if serializer.is_valid():
            request_id = serializer.validated_data['request_id']
            action = serializer.validated_data['action']

            try:
                host_request = HostRequest.objects.get(id=request_id)
            except HostRequest.DoesNotExist:
                return Response({"error": "Host request not found."}, status=status.HTTP_404_NOT_FOUND)

            if action == 'accept':
                host_request.request_status = HostRequest.APPROVED
                new_host_data = {
                    'person': host_request.user.id,
                    'email': host_request.user.email,
                    'password': host_request.user.password,
                    'host_approval_status': 'Approved', 
                    'property_address': host_request.property_address,
                    'property_type': host_request.property_type,
                    'description': host_request.description,
                    'amenities': host_request.amenities,
                    'property_name': host_request.property_name,
                }
                new_host_serializer = HostSerializer(data=new_host_data)
                if new_host_serializer.is_valid():
                    new_host_serializer.save()
                else:
                    return Response(new_host_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                user = host_request.user
                user.role = 'host'
                user.save()

            elif action == 'reject':
                host_request.request_status = "Rejected"

            host_request.save()
            return Response({"message": f"Host request {request_id} {action}ed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)