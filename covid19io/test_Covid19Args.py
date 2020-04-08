from unittest import TestCase
from covid19io.Covid19Args import Covid19Args


class TestCovid19Args(TestCase):
    def test__get_location_args(self):
        def test1():
            self.assertEqual([], Covid19Args._getLocationArgs(''))

        def test2():
            self.assertEqual([], Covid19Args._getLocationArgs('abc'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc.def'))
            self.assertEqual([], Covid19Args._getLocationArgs(' abc   '))
            self.assertEqual([], Covid19Args._getLocationArgs('/abc'))
            self.assertEqual([], Covid19Args._getLocationArgs('   /abc'))
            self.assertEqual([], Covid19Args._getLocationArgs(' / abc'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc/'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc  /'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc  / '))
            self.assertEqual([], Covid19Args._getLocationArgs('abc   /'))
            self.assertEqual(['abc/def'], Covid19Args._getLocationArgs('abc/def'))
            self.assertEqual(['abc / def'], Covid19Args._getLocationArgs('abc / def'))
            self.assertEqual(['abc /def'], Covid19Args._getLocationArgs('abc /def'))
            self.assertEqual(['abc xyz/def'], Covid19Args._getLocationArgs('abc xyz/def'))

        def test3():
            self.assertEqual([], Covid19Args._getLocationArgs('abc, def'))
            self.assertEqual(['abc/xyz'], Covid19Args._getLocationArgs('abc/xyz, def'))
            self.assertEqual(['abc/xyz', 'def/ghi'], Covid19Args._getLocationArgs('abc/xyz, def/ghi'))
            self.assertEqual(['abc/xyz', 'def jkl/ghi'], Covid19Args._getLocationArgs('abc/xyz, "def jkl"/ghi'))
            self.assertEqual(['abc/xyz', 'def jkl/ghi', 'mno /pqr'],
                             Covid19Args._getLocationArgs('abc/xyz, "def jkl"/ghi, xyz, mno /pqr'))

        test1()
        test2()
        test3()

    def test_setup(self):

        pass
