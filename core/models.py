from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(null=True, max_length=255)
    county = models.CharField(null=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'city', 'county')


class Visa(models.Model):
    type = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, related_name='visas', on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('type', 'route', 'organization')
