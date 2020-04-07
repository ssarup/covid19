from unittest import TestCase
from data.Observation import Observation
from data.ObservationDate import ObservationDate


class TestObservation(TestCase):
    def test_creation(self):
        d = ObservationDate.fromMDY('2/1/2020')
        t = Observation(d, 5)
        self.assertIsNotNone(t)
        self.assertEqual(t._obsDate._value, ObservationDate.fromMDY("2/1/2020")._value)
        self.assertEqual(t._value, 5)

        t._obsDate = ObservationDate.fromMDY("3/1/2020")
        self.assertEqual(t._value, 5)

        t._value = 6
        self.assertEqual(t._value, 6)

        v = t
        self.assertEqual(t, v)
        self.assertEqual(v, t)

        v._value = 6.1
        self.assertEqual(t, v)
        self.assertEqual(v, t)


