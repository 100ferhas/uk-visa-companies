from rest_framework import serializers

from core.models import Organization, Visa


class VisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = ['type', 'route', ]


class OrganizationSerializer(serializers.ModelSerializer):
    visas = VisaSerializer(many=True, read_only=True)
    detail = serializers.HyperlinkedIdentityField(view_name='organization-detail')

    class Meta:
        model = Organization
        fields = ['id', 'name', 'city', 'county', 'detail', 'visas', ]
