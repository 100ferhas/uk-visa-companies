from django.contrib import admin

from core.models import Organization, Visa


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ["name", "city", "county"]
    list_display = ["name", "city", "county", "get_visas"]

    @admin.display(description='Visas')
    def get_visas(self, obj):
        return ", ".join([v.route for v in obj.visas.all()])


@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    list_display = ["organization", "route", "type"]
    list_filter = ["route", "type"]
    search_fields = ["organization"]
