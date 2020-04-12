from unittest import TestCase
from math import log
from data.Observation import Observation
from data.ObservationDate import ObservationDate


class TestObservation(TestCase):
    def test_creation(self):
        d = ObservationDate.fromMDY('2/1/2020')
        t = Observation(d, 5)
        self.assertIsNotNone(t)
        self.assertEqual(t._obsDate._value, ObservationDate.fromMDY("2/1/2020")._value)
        self.assertEqual(t._value, 5)
        log2OfVal = log(5, 2)
        lnOfVal = log(5)
        self.assertEqual('02/01/2020', t.obsDate.value.strftime('%m/%d/%Y'))
        self.assertEqual(5, t.value)
        self.assertEqual(log2OfVal, t.log2Value)
        self.assertEqual(lnOfVal, t.lnValue)

        t._obsDate = ObservationDate.fromMDY("3/1/2020")
        self.assertEqual(t._value, 5)
        self.assertEqual(log2OfVal, t.log2Value)
        self.assertEqual(lnOfVal, t.lnValue)

        t._value = 6
        self.assertEqual(t._value, 6)
        self.assertEqual(log2OfVal, t.log2Value)
        self.assertEqual(lnOfVal, t.lnValue)

        v = t
        self.assertEqual(t, v)
        self.assertEqual(v, t)
        self.assertEqual(log2OfVal, v.log2Value)
        self.assertEqual(lnOfVal, v.lnValue)

        v._value = 6.1
        self.assertEqual(t, v)
        self.assertEqual(v, t)
        self.assertEqual(log2OfVal, v.log2Value)
        self.assertEqual(lnOfVal, v.lnValue)

        def testLogValues():
            t = Observation(d, -1)
            self.assertIsNone(t.log2Value)
            self.assertIsNone(t.lnValue)
            t = Observation(d, 0)
            self.assertIsNone(t.log2Value)
            self.assertIsNone(t.lnValue)
            t = Observation(d, 1)
            self.assertEqual(log(1, 2), t.log2Value)
            self.assertEqual(log(1), t.lnValue)
            t = Observation(d, 10)
            self.assertEqual(log(10, 2), t.log2Value)
            self.assertEqual(log(10), t.lnValue)

        testLogValues()




