from unittest import TestCase
import datetime
from data.ObservationDate import ObservationDate


class TestDateValue(TestCase):
    def test_from_mdy(self):
        def createDateValue(str_):
            return ObservationDate.fromMDY(str_)

        self.assertIsNotNone(createDateValue('1/1/2020'))
        self.assertIsNotNone(createDateValue('01/1/2020'))
        self.assertIsNotNone(createDateValue('1/01/2020'))
        self.assertIsNotNone(createDateValue('01/01/2020'))
        self.assertIsNotNone(createDateValue('12/1/2020'))
        self.assertIsNotNone(createDateValue('12/31/2020'))
        self.assertIsNone(createDateValue('1/32/2020'))
        self.assertIsNone(createDateValue('12/32/2020'))
        self.assertIsNone(createDateValue('13/1/2020'))
        self.assertIsNone(createDateValue('13'))
        self.assertIsNone(createDateValue('a'))
        self.assertIsNone(createDateValue(''))
        self.assertIsNone(createDateValue(None))

        a = createDateValue('1/1/2020')
        self.assertEqual(a._value, datetime.datetime.strptime('1/1/2020', '%m/%d/%Y'))

        b = createDateValue('1/1/2020')
        self.assertEqual(a._value, b._value)

        c = createDateValue('2/1/2020')
        self.assertNotEqual(a._value, c._value)
        self.assertNotEqual(b._value, c._value)

    def test_from_mdy2(self):
        def createDateValue(str_):
            return ObservationDate.fromMDY2(str_)

        self.assertIsNotNone(createDateValue('1/1/20'))
        self.assertIsNotNone(createDateValue('01/1/20'))
        self.assertIsNotNone(createDateValue('1/01/20'))
        self.assertIsNotNone(createDateValue('01/01/20'))
        self.assertIsNotNone(createDateValue('12/1/20'))
        self.assertIsNotNone(createDateValue('12/31/20'))
        self.assertIsNone(createDateValue('1/32/20'))
        self.assertIsNone(createDateValue('12/32/20'))
        self.assertIsNone(createDateValue('13/1/20'))
        self.assertIsNone(createDateValue('13'))
        self.assertIsNone(createDateValue('a'))
        self.assertIsNone(createDateValue(''))
        self.assertIsNone(createDateValue(None))

        a = createDateValue('1/1/20')
        self.assertEqual(a._value, datetime.datetime.strptime('1/1/20', '%m/%d/%y'))

        b = createDateValue('1/1/20')
        self.assertEqual(a._value, b._value)

        c = createDateValue('2/1/20')
        self.assertNotEqual(a._value, c._value)
        self.assertNotEqual(b._value, c._value)

