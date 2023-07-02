import csv

from core.models import Organization, Visa


def sync_gov_data():
    visas = list()
    Visa.objects.all().update(deleted=True)

    with open('2023-06-30_-_Worker_and_Temporary_Worker.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip header

        for row in csv_reader:
            organization = Organization.objects.get_or_create(name=row[0], city=row[1], county=row[2])[0]
            visas.append(Visa(type=row[3], route=row[4], organization=organization))

    Visa.objects.bulk_create(
        visas, update_conflicts=True, unique_fields=['type', 'route', 'organization'], update_fields=['deleted'],
    )
    Visa.objects.filter(deleted=True).delete()
    Organization.objects.filter(visas__isnull=True).delete()
