from unittest import TestCase
from data.LocationDoNotUse import LocationDoNotUse


class TestLocationDoNotUse(TestCase):
    def test_empty(self):
        self.assertIsNone(LocationDoNotUse()._country)
        self.assertIsNone(LocationDoNotUse()._state)
        self.assertIsNone(LocationDoNotUse()._county)
        self.assertIsNone(LocationDoNotUse()._city)

    def test_country(self):
        t = LocationDoNotUse()
        self.assertIsNone(t._country)
        self.assertIsNone(t.country(None)._country)
        self.assertEqual(t.country("abc")._country, "abc")
        self.assertEqual(t.country(1)._country, 1)
        self.assertEqual(LocationDoNotUse().country("abc")._country, "abc")
        self.assertIsNone(LocationDoNotUse().country(None)._country)
        self.assertEqual(LocationDoNotUse().country(1)._country, t._country)
        self.assertEqual(LocationDoNotUse().state(10).country(1)._country, t._country)
        self.assertEqual(LocationDoNotUse().county(100).country(1)._country, t._country)
        self.assertEqual(LocationDoNotUse().city(1000).country(1)._country, t._country)
        self.assertEqual(LocationDoNotUse().state(20).county(200).city(2000).country(1)._country, t._country)
        self.assertEqual(t._country, 1)

    def test_state(self):
        t = LocationDoNotUse()
        self.assertIsNone(t._state)
        self.assertIsNone(t.state(None)._state)
        self.assertEqual(t.state("abc")._state, "abc")
        self.assertEqual(t.state(1)._state, 1)
        self.assertEqual(LocationDoNotUse().state("abc")._state, "abc")
        self.assertIsNone(LocationDoNotUse().state(None)._state)
        self.assertEqual(LocationDoNotUse().state(1)._state, t._state)
        self.assertEqual(t._state, 1)

    def test_county(self):
        t = LocationDoNotUse()
        self.assertIsNone(t._county)
        self.assertIsNone(t.county(None)._county)
        self.assertEqual(t.county("abc")._county, "abc")
        self.assertEqual(t.county(1)._county, 1)
        self.assertEqual(LocationDoNotUse().county("abc")._county, "abc")
        self.assertIsNone(LocationDoNotUse().county(None)._county)
        self.assertEqual(LocationDoNotUse().county(1)._county, t._county)
        self.assertEqual(t._county, 1)

    def test_city(self):
        t = LocationDoNotUse()
        self.assertIsNone(t._city)
        self.assertIsNone(t.city(None)._city)
        self.assertEqual(t.city("abc")._city, "abc")
        self.assertEqual(t.city(1)._city, 1)
        self.assertEqual(LocationDoNotUse().city("abc")._city, "abc")
        self.assertIsNone(LocationDoNotUse().city(None)._city)
        self.assertEqual(LocationDoNotUse().city(1)._city, t._city)
        self.assertEqual(t._city, 1)

    def test_equality(self):
        t = LocationDoNotUse()
        u = LocationDoNotUse()
        self.assertNotEqual(t, u)