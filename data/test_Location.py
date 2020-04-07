from unittest import TestCase
from data.Location import Location


class TestLocation(TestCase):
    def test_empty(self):
        self.assertIsNone(Location()._country)
        self.assertIsNone(Location()._state)
        self.assertIsNone(Location()._county)
        self.assertIsNone(Location()._city)

    def test_country(self):
        t = Location()
        self.assertIsNone(t._country)
        self.assertIsNone(t.country(None)._country)
        self.assertEqual(t.country("abc")._country, "abc")
        self.assertEqual(t.country(1)._country, 1)
        self.assertEqual(Location().country("abc")._country, "abc")
        self.assertIsNone(Location().country(None)._country)
        self.assertEqual(Location().country(1)._country, t._country)
        self.assertEqual(Location().state(10).country(1)._country, t._country)
        self.assertEqual(Location().county(100).country(1)._country, t._country)
        self.assertEqual(Location().city(1000).country(1)._country, t._country)
        self.assertEqual(Location().state(20).county(200).city(2000).country(1)._country, t._country)
        self.assertEqual(t._country, 1)

    def test_state(self):
        t = Location()
        self.assertIsNone(t._state)
        self.assertIsNone(t.state(None)._state)
        self.assertEqual(t.state("abc")._state, "abc")
        self.assertEqual(t.state(1)._state, 1)
        self.assertEqual(Location().state("abc")._state, "abc")
        self.assertIsNone(Location().state(None)._state)
        self.assertEqual(Location().state(1)._state, t._state)
        self.assertEqual(t._state, 1)

    def test_county(self):
        t = Location()
        self.assertIsNone(t._county)
        self.assertIsNone(t.county(None)._county)
        self.assertEqual(t.county("abc")._county, "abc")
        self.assertEqual(t.county(1)._county, 1)
        self.assertEqual(Location().county("abc")._county, "abc")
        self.assertIsNone(Location().county(None)._county)
        self.assertEqual(Location().county(1)._county, t._county)
        self.assertEqual(t._county, 1)

    def test_city(self):
        t = Location()
        self.assertIsNone(t._city)
        self.assertIsNone(t.city(None)._city)
        self.assertEqual(t.city("abc")._city, "abc")
        self.assertEqual(t.city(1)._city, 1)
        self.assertEqual(Location().city("abc")._city, "abc")
        self.assertIsNone(Location().city(None)._city)
        self.assertEqual(Location().city(1)._city, t._city)
        self.assertEqual(t._city, 1)

    def test_equality(self):
        t = Location()
        u = Location()
        self.assertEqual(t, u)