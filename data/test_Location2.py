from unittest import TestCase

from data.Location2 import Location2


class TestLocation2(TestCase):
    def test_country(self):
        loc = Location2()
        self.assertIsNone(loc.country)
        loc = Location2('abc')
        self.assertIsNotNone(loc)
        self.assertEqual('abc', loc.country)
        self.assertNotEqual('abcd', loc.country)

    def test_state(self):
        loc = Location2()
        self.assertIsNone(loc._state)
        loc = Location2(None, 'NY')
        self.assertEqual('NY', loc._state)
        self.assertNotEqual('NJ', loc._state)
        loc._state = 'CA'
        self.assertEqual('CA', loc._state)
        loc._country = 'US'
        self.assertEqual('CA', loc._state)
        l1 = Location2('US', 'CA')
        self.assertEqual(loc, l1)

    def test_county(self):
        loc = Location2()
        self.assertIsNone(loc._county)
        loc = Location2(None, None, 'Rockland')
        self.assertEqual('Rockland', loc._county)
        self.assertNotEqual('Middlesex', loc._county)
        loc._county = 'Hudson'
        self.assertEqual('Hudson', loc._county)
        loc._country = 'US'
        loc._state = 'NY'
        self.assertEqual('Hudson', loc._county)
        l1 = Location2('US', 'NY', 'Hudson')
        self.assertEqual(loc, l1)

    def test_state(self):
        loc = Location2()
        self.assertIsNone(loc._city)
        loc = Location2(None, None, None, 'New City')
        self.assertEqual('New City', loc._city)
        self.assertNotEqual('Nanuet', loc._city)
        loc._city = 'Ramapo'
        self.assertEqual('Ramapo', loc._city)
        loc._country = 'US'
        loc._state = 'NY'
        loc._county = 'Rockland'
        self.assertEqual('Ramapo', loc._city)
        l1 = Location2('US', 'NY', 'Rockland', 'Ramapo')
        self.assertEqual(loc, l1)

    def test_equal(self):
        def test1():
            # Test for None
            l = Location2()
            self.assertNotEqual(None, l)
            self.assertEqual(Location2(), l)
            self.assertEqual(l, l)
            self.assertNotEqual('', l)
            l1 = Location2()
            self.assertEqual(l1, l)
            l1._country = None
            self.assertEqual(l1, l)
            l1._country = ''
            self.assertNotEqual(l1, l)
            l1 = l
            self.assertEqual(l1, l)
            l1 = Location2(None)
            self.assertEqual(l1, l)

        def test2():
            # Test for value
            l = Location2('')
            self.assertEqual(l, l)
            self.assertNotEqual('', l)
            self.assertNotEqual('[ ,country =  ,]', l)
            self.assertNotEqual(Location2, l)
            self.assertEqual(Location2(''), l)
            l1 = Location2('')
            self.assertEqual(l1, l)
            l1._country = 'abc'
            self.assertNotEqual(l1, l)
            l1._country = l._country
            self.assertEqual(l1, l)
            l1 = Location2(state_='')
            self.assertNotEqual(l1, l)
            l2 = Location2()
            l2._state = ''
            self.assertEqual(l1, l2)
            self.assertNotEqual(l2, l)
            l2._country = 'abc'
            self.assertNotEqual(l2, l1)
            l1._country = 'abc'
            self.assertEqual(l2, l1)
            l1._state = 'NY'
            self.assertNotEqual(l2, l1)
            self.assertEqual(l1, l1)
            l2._state = l1._state
            self.assertEqual(l2, l1)
            self.assertEqual(Location2(country_='abc', state_='NY'), l1)
            l1._county = 'Rockland'
            l1._city = 'New City'
            self.assertNotEqual(l2, l1)
            self.assertEqual(l1, l1)
            l2._city = l1._city
            self.assertNotEqual(l2, l1)
            l2._state = l1._state
            self.assertNotEqual(l2, l1)
            l2._county = l1._county
            self.assertEqual(l2, l1)
            l1._country = 'US'
            self.assertNotEqual(l2, l1)
            self.assertNotEqual(Location2(country_='US', state_='NY'), l1)
            self.assertNotEqual(Location2(country_='US', state_='NY', county_='Rockland'), l1)
            self.assertEqual(Location2(country_='US', state_='NY', county_='Rockland', city_='New City'), l1)

        test1()
        test2()

    def test_hash(self):
        def test1():
            h = hash(Location2())
            self.assertEqual(h, h)
            l = Location2()
            self.assertEqual(Location2(), l)
            self.assertEqual(h, hash(l))
            l._country = None
            self.assertEqual(h, hash(l))
            l1 = Location2()
            h1 = hash(l1)
            self.assertEqual(h1, h)
            l1._country = None
            self.assertEqual(h1, hash(l1))
            l1._country = ''
            self.assertNotEqual(h1, hash(l1))
            l1._country = 'abc'
            self.assertNotEqual(h1, hash(l1))
            h1 = hash(l1)
            self.assertEqual(h1, hash(l1))
            l2 = Location2(country_='abc')
            self.assertEqual(h1, hash(l2))
            l2._state = 'NY'
            l2._county = 'Rockland'
            l2._city = 'New City'
            self.assertNotEqual(l1, l2)
            self.assertNotEqual(h1, hash(l2))
            self.assertEqual(hash(Location2(country_='abc', state_='NY', county_='Rockland', city_='New City')), hash(l2))

        test1()