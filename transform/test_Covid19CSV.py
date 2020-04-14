import datetime
from unittest.case import TestCase

from transform.Covid19CSV import Covid19CSV


class TestCovid19CSV(TestCase):
    @staticmethod
    def _createDateValueData(numEntries_):
        date2Val = {}
        dateList = []
        valueList = []
        startDt = datetime.datetime.strptime('1/1/2020', '%m/%d/%Y')
        for i in range(0, numEntries_):
            dt = startDt + datetime.timedelta(days=i)
            dtStr = dt.strftime('%m/%d/%Y')
            date2Val[dtStr] = i
            dateList.append(dtStr)
            valueList.append(i)
        return date2Val, dateList, tuple(valueList)

    @staticmethod
    def _compare2Hashes(h1_, h2_):
        retVal = len(h1_.keys()) == len(h2_.keys())
        s1 = set(h1_.keys())
        s2 = set(h2_.keys())
        retVal = retVal and len(s1) == len(s2)
        retVal = retVal and len(s1.union(s2)) == len(s2)
        retVal = retVal and len(s1.intersection(s2)) == len(s2)
        for k in h1_.keys():
            retVal = retVal and h1_[k] == h2_[k]
        return retVal

    def setUp(self):
        self._NUM_ENTRIES = 10
        (self._date2Val, self._dateList, self._valueTuple) = TestCovid19CSV._createDateValueData(self._NUM_ENTRIES)

    def test_set_date2value(self):
        o1 = Covid19CSV('abc', 'def', 'ghi')
        self.assertEqual(o1._country, 'abc')
        self.assertEqual(o1._state, 'def')
        self.assertEqual(o1._county, 'ghi')
        self.assertEqual(len(o1._dateList), 0)
        self.assertEqual(len(o1._date2Value.keys()), 0)

        self.assertEqual(len(self._date2Val.keys()), self._NUM_ENTRIES)
        self.assertEqual(len(self._dateList), self._NUM_ENTRIES)
        self.assertEqual(len(self._valueTuple), self._NUM_ENTRIES)

        o1.setDate2Value(self._dateList, self._valueTuple)
        self.assertEqual(len(o1._dateList), self._NUM_ENTRIES)
        self.assertEqual(len(o1._date2Value.keys()), self._NUM_ENTRIES)
        self.assertTrue(self._compare2Hashes(self._date2Val, o1._date2Value))

        o1.setDate2Value(self._dateList[:len(self._dateList) - 1], self._valueTuple)
        self.assertEqual(self._NUM_ENTRIES - 1, len(o1._dateList))
        self.assertEqual(self._NUM_ENTRIES - 1, len(o1._date2Value.keys()))

        o1.setDate2Value(self._dateList, self._valueTuple[:len(self._valueTuple) - 1])
        self.assertEqual(self._NUM_ENTRIES - 1, len(o1._dateList))
        self.assertEqual(self._NUM_ENTRIES - 1, len(o1._date2Value.keys()))