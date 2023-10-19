from django.test import TestCase
from .models import Location

class LocationModelTestCase(TestCase):
    def test_calculate_distance(self):
        location1 = Location.objects.create(
            name='Location 1',
            latitude=37.123456,
            longitude=-122.987654,
        )
        location2 = Location.objects.create(
            name='Location 2',
            latitude=38.123456,
            longitude=-123.987654,
        )

        distance = location1.calculate_distance(location2)

        expected_distance = 141.84554102357347

        self.assertAlmostEqual(distance, expected_distance, places=1)

    def test_str_representation(self):
        location = Location.objects.create(
            name='Test Location',
            latitude=37.123456,
            longitude=-122.987654,
        )

        self.assertEqual(str(location), 'Test Location')

    def test_location_to_dict(self):
        location = Location.objects.create(
            name='Test Location',
            latitude=37.123456,
            longitude=-122.987654,
        )

        location_dict = {
            'name': location.name,
            'latitude': float(location.latitude),
            'longitude': float(location.longitude),
        }

        expected_dict = {
            'name': 'Test Location',
            'latitude': 37.123456,
            'longitude': -122.987654,
        }

        self.assertEqual(location_dict, expected_dict)
