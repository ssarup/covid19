from unittest import TestCase

from data.Location import Location


class TestLocation(TestCase):
    def test_country(self):
        loc = Location()
        self.assertIsNone(loc.country)
        loc = Location('abc')
        self.assertIsNotNone(loc)
        self.assertEqual('abc', loc.country)
        self.assertNotEqual('abcd', loc.country)
        loc.country = 'xyz'
        self.assertEqual('abc', loc.country)
        self.assertNotEqual('xyz', loc.country)

    def test_state(self):
        loc = Location()
        self.assertIsNone(loc._state)
        loc = Location(None, 'NY')
        self.assertEqual('NY', loc._state)
        self.assertNotEqual('NJ', loc._state)
        loc._state = 'CA'
        self.assertEqual('CA', loc._state)
        loc._country = 'US'
        self.assertEqual('CA', loc._state)
        l1 = Location('US', 'CA')
        self.assertEqual(loc, l1)
        l1 = Location('US', 'New Jersey')
        self.assertEqual('New Jersey', l1.state)
        self.assertEqual(Location('US', 'New Jersey'), l1)
        l1.state = 'NJ'
        self.assertNotEqual('NJ', l1.state)
        self.assertEqual('New Jersey', l1.state)

    def test_county(self):
        loc = Location()
        self.assertIsNone(loc._county)
        loc = Location(None, None, 'Rockland')
        self.assertEqual('Rockland', loc._county)
        self.assertNotEqual('Middlesex', loc._county)
        loc._county = 'Hudson'
        self.assertEqual('Hudson', loc._county)
        loc._country = 'US'
        loc._state = 'NY'
        self.assertEqual('Hudson', loc._county)
        l1 = Location('US', 'NY', 'Hudson')
        self.assertEqual(loc, l1)
        l1.county = 'Orange'
        self.assertNotEqual('Orange', l1.county)
        self.assertEqual('Hudson', l1.county)

    def test_city(self):
        loc = Location()
        self.assertIsNone(loc._city)
        loc = Location(None, None, None, 'New City')
        self.assertEqual('New City', loc._city)
        self.assertNotEqual('Nanuet', loc._city)
        loc._city = 'Ramapo'
        self.assertEqual('Ramapo', loc._city)
        loc._country = 'US'
        loc._state = 'NY'
        loc._county = 'Rockland'
        self.assertEqual('Ramapo', loc._city)
        l1 = Location('US', 'NY', 'Rockland', 'Ramapo')
        self.assertEqual(loc, l1)
        l1.city = 'Monroe'
        self.assertNotEqual('Monroe', l1.city)
        self.assertEqual('Ramapo', l1.city)

    def test_equal(self):
        def test1():
            # Test for None
            l = Location()
            self.assertNotEqual(None, l)
            self.assertEqual(Location(), l)
            self.assertEqual(l, l)
            self.assertNotEqual('', l)
            l1 = Location()
            self.assertEqual(l1, l)
            l1._country = None
            self.assertEqual(l1, l)
            l1._country = ''
            self.assertNotEqual(l1, l)
            l1 = l
            self.assertEqual(l1, l)
            l1 = Location(None)
            self.assertEqual(l1, l)
            l1 = Location('', '', '')
            self.assertNotEqual(10, l1)

        def test2():
            # Test for value
            l = Location('')
            self.assertEqual(l, l)
            self.assertNotEqual('', l)
            self.assertNotEqual('[ ,country =  ,]', l)
            self.assertNotEqual(Location, l)
            self.assertEqual(Location(''), l)
            l1 = Location('')
            self.assertEqual(l1, l)
            l1._country = 'abc'
            self.assertNotEqual(l1, l)
            l1._country = l._country
            self.assertEqual(l1, l)
            l1 = Location(state_='')
            self.assertNotEqual(l1, l)
            l2 = Location()
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
            self.assertEqual(Location(country_='abc', state_='NY'), l1)
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
            self.assertNotEqual(Location(country_='US', state_='NY'), l1)
            self.assertNotEqual(Location(country_='US', state_='NY', county_='Rockland'), l1)
            self.assertEqual(Location(country_='US', state_='NY', county_='Rockland', city_='New City'), l1)

        test1()
        test2()

    def test_hash(self):
        def test1():
            h = hash(Location())
            self.assertEqual(h, h)
            l = Location()
            self.assertEqual(Location(), l)
            self.assertEqual(h, hash(l))
            l._country = None
            self.assertEqual(h, hash(l))
            l1 = Location()
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
            l2 = Location(country_='abc')
            self.assertEqual(h1, hash(l2))
            l2._state = 'NY'
            l2._county = 'Rockland'
            l2._city = 'New City'
            self.assertNotEqual(l1, l2)
            self.assertNotEqual(h1, hash(l2))
            self.assertEqual(hash(Location(country_='abc', state_='NY', county_='Rockland', city_='New City')), hash(l2))

        test1()