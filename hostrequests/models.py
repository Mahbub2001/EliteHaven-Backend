# models.py
from django.db import models
from django.contrib.auth import get_user_model

class HostRequest(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    request_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    request_date = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='admin_responses', null=True, blank=True)
    response_date = models.DateTimeField(null=True, blank=True)
    property_address = models.CharField(max_length=255, default='')
    property_type = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    amenities = models.TextField(default='')
    property_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return f'Request {self.id} by {self.user}'

class Host(models.Model):
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    host_approval_status = models.CharField(max_length=50)
    property_address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=100)
    description = models.TextField()
    amenities = models.TextField()
    property_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.person}'
