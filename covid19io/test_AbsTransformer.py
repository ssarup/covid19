from unittest import TestCase
from covid19io.AbsTransformer import AbsTransformer


class TestAbsTransformer(TestCase):
    class MyObj(object):
        pass

    class MyTransformer1(AbsTransformer):
        def __init__(self):
            self._header = ['id', 'state', 'country', 'val']
            self._colsToRead = []
            self._coll = []

        def processHeader(self, colsAsTuple_):
            self._colsToRead = []
            for hdr in self._header:
                if hdr in colsAsTuple_:
                    colNum = colsAsTuple_.index(hdr)
                    self._colsToRead.append(colNum)

        def columnsToRead(self):
            return self._colsToRead

        def createObject(self, colsAsTuple_):
            # print('yy', str(colsAsTuple_))
            o1 = TestAbsTransformer.MyObj()
            o1._val1 = colsAsTuple_[0]
            o1._val2 = colsAsTuple_[1]
            # print('zz: {0} {1}'.format(o1._val1, o1._val2))
            return o1

        def addToCollection(self, obj_):
            self._coll.append(obj_)

        def getCollection(self):
            return self._coll


    def setUp(self):
        self._line = [
            (1, 'US', 'NY', 'Rockland', 10),
            (2, 'US', 'NY', 'Rockland', 20),
            (3, 'US', 'NY', 'Westchester', 30),
            (4., 'US', 'NJ', 'Middlesex', 40)
        ]

    def test_process_header(self):
        def test1(tx_):
            hdr = 'id,country,state,val'
            tx_.processHeader(tuple(hdr.split(',')))
            self.assertEqual(4, len(t1._colsToRead))

        def test2(tx_):
            hdr = 'id,country,state,val,date'
            tx_.processHeader(tuple(hdr.split(',')))
            self.assertEqual(4, len(t1._colsToRead))

        def test3(tx_):
            hdr = 'id,country,state'
            tx_.processHeader(tuple(hdr.split(',')))
            self.assertEqual(3, len(t1._colsToRead))

        t1 = TestAbsTransformer.MyTransformer1()
        test1(t1)
        test2(t1)
        test3(t1)

    def test_columns_to_read(self):
        hdr = 'id,country,state,val,date'
        hdrAsTuple = tuple(hdr.split(','))
        t1 = TestAbsTransformer.MyTransformer1()
        t1.processHeader(hdrAsTuple)
        self.assertEqual(len(t1._header), len(t1.columnsToRead()))
        self.assertEqual([0, 2, 1, 3], t1.columnsToRead())

    def test_create_object(self):
        t1 = TestAbsTransformer.MyTransformer1()
        o1 = t1.createObject(('US', 'NJ'))
        self.assertEqual(o1._val1, 'US')
        self.assertEqual(o1._val2, 'NJ')

    def test_add_to_collection(self):
        t1 = TestAbsTransformer.MyTransformer1()
        o1 = t1.createObject(('US', 'NJ'))
        t1.addToCollection(o1)
        self.assertEqual(len(t1._coll), 1)
        self.assertEqual(t1._coll[0]._val1, 'US')
        self.assertEqual(t1._coll[0]._val2, 'NJ')

    def test_get_collection(self):
        t1 = TestAbsTransformer.MyTransformer1()
        o1 = t1.createObject(('US', 'NJ'))
        t1.addToCollection(o1)
        c1 = t1.getCollection()
        self.assertEqual(len(c1), 1)
        self.assertEqual(c1[0]._val1, 'US')
        self.assertEqual(c1[0]._val2, 'NJ')

    def test_process_line(self):
        t1 = TestAbsTransformer.MyTransformer1()
        i = 0
        # (1, 'US', 'NY', 'Rockland', 10),
        t1.processLine(['id', 'country', 'state', 'county', 'val'], True)
        for line in self._line:
            t1.processLine(line, False)
            self.assertEqual(len(t1.getCollection()), i + 1)
            # obj = t1.getCollection()[i]
            # print('xx: {0}: {1} {2}'.format(i, obj._val1, obj._val2))
            self.assertEqual(t1.getCollection()[i]._val1, self._line[i][0])
            self.assertEqual(t1.getCollection()[i]._val2, self._line[i][2])
            i = i + 1

