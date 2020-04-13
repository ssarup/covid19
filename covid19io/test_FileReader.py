from unittest import TestCase
from covid19io.FileReader import FileReader
from covid19io.AbsTransformer import AbsTransformer


class TestFileReader(TestCase):

    class MyObj(object):
        pass

    class MyTransformer1(AbsTransformer):
        def __init__(self):
            # self._header = ['country', 'state', 'county']
            self._colToRead = []
            self._coll = []

        def processHeader(self, headerColsList_):
            self._colToRead = [2, 6, 5]

        def listOfIndexesOfColumnsToRead(self):
            return self._colToRead

        def createObject(self, colsAsTuple_):
            o1 = TestFileReader.MyObj()
            o1._val1 = colsAsTuple_[0]
            o1._val2 = colsAsTuple_[1]
            return o1

        def addToCollection(self, obj_):
            self._coll.append(obj_)

        def getCollection(self):
            return self._coll


    def test_read(self):
        def test1():
            rdr = FileReader(None)
            self.assertIsNone(rdr._fName)
            self.assertIsNone(rdr._fHandle)

        def test2():
            rdr = FileReader('abc')
            self.assertEqual('abc', rdr._fName)
            self.assertIsNone(rdr._fHandle)

        def test3():
            rdr = FileReader('/Users/developer/Downloads')
            tx = TestFileReader.MyTransformer1()
            self.assertEqual(0, len(tx._coll))
            try:
                rdr.read(tx)
            except:
                pass
            self.assertEqual('/Users/developer/Downloads', rdr._fName)
            self.assertIsNone(rdr._fHandle)
            self.assertEqual(0, len(tx._coll))

        def test4():
            rdr = FileReader('/Users/developer/Downloads/time_series_covid19_confirmed_US-2.csv')
            tx = TestFileReader.MyTransformer1()
            self.assertEqual(0, len(tx._coll))
            rdr.read(tx)
            self.assertEqual('/Users/developer/Downloads/time_series_covid19_confirmed_US-2.csv', rdr._fName)
            self.assertIsNone(rdr._fHandle)
            self.assertEqual(3253, len(tx._coll))

        test1()
        test2()
        test3()
        test4()
