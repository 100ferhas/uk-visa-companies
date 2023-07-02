from django.test import TestCase

from core import cron


class CronTestCase(TestCase):
    # def setUp(self):
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    def test_file_import(self):
        """Import CSV File"""
        cron.sync_gov_data()
