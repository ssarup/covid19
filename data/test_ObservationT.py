from unittest import TestCase
from data.ObservationT import ObservationT


class TestObservationT(TestCase):
    def test_creation(self):
        t = ObservationT.CASES
        self.assertEqual(t, ObservationT.CASES)
        self.assertNotEqual(t, ObservationT.DEATHS)
        self.assertNotEqual(t, ObservationT.RECOVERED)

        u = ObservationT.DEATHS
        v = ObservationT.DEATHS
        self.assertNotEqual(u, t)
        self.assertNotEqual(u, ObservationT.CASES)
        self.assertEqual(u, u)
        self.assertEqual(u, v)
        self.assertEqual(v, u)
        self.assertEqual(u, ObservationT.DEATHS)

        v = ObservationT.RECOVERED
        self.assertNotEqual(u, v)
        self.assertEqual(v, ObservationT.RECOVERED)

        def testSwitch(obsT_):
            switcher = {
                ObservationT.CASES: 10,
                ObservationT.DEATHS: 20,
                ObservationT.RECOVERED: 30
            }
            return switcher.get(obsT_)

        self.assertEqual(testSwitch(ObservationT.CASES), 10)
        self.assertEqual(testSwitch(ObservationT.RECOVERED), 30)
        self.assertNotEqual(testSwitch(ObservationT.DEATHS), 10)
