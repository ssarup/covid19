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

        loc1 = Location2('abc')
        self.assertEqual(loc1, loc)
        # self.assertNotEqual(Location2('abc', 'bcd'), loc)
        # self.assertEqual(Location2(), loc)

    # def test_state(self):
    #     self.fail()
    #
    # def test_country(self):
    #     self.fail()
    #
    # def test_state(self):
    #     self.fail()
    #
    # def test_county(self):
    #     self.fail()
    #
    # def test_county(self):
    #     self.fail()
    #
    # def test_city(self):
    #     self.fail()
    #
    # def test_city(self):
    #     self.fail()

    def test_equal(self):
        def test1():
            # Test for None
            l = Location2()
            self.assertNotEqual(None, l)
            self.assertEqual(Location2(), l)
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
            l2._state = l1._state
            self.assertEqual(l2, l1)

        test1()
        test2()