from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from core.models import Organization
from core.serializers import OrganizationSerializer


class OrganizationViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, ]
    # filterset_fields = ["name", "city", "county", ]
    search_fields = ["$name", "$city", ]
    serializer_class = OrganizationSerializer
    ordering_fields = ['name', 'city']
    ordering = ['name']
