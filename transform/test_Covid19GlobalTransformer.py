from unittest import TestCase
import csv
from transform.Covid19CSV import Covid19CSV
from transform.Covid19GlobalTransformer import Covid19GlobalTransformer


class TestCovid19GlobalTransformer(TestCase):
    def test_col_names_icare(self):
        tx = Covid19GlobalTransformer()
        verifyList = ['Country/Region', 'Province/State']
        self.assertEqual(verifyList, tx.listOfColumnNamesToRead())

    def test_last_col_name_before_dates(self):
        tx = Covid19GlobalTransformer()
        self.assertEqual('Long', tx.lastColNameBeforeDates())

    @staticmethod
    def _createVerificationObject(hdr_, str_):
        # Input string may have embedded commas in a field.
        # 'aaa, bbb, "ccc, ddd", eee'
        strAsList = list(csv.reader([str_], delimiter=',', quotechar='"', skipinitialspace=True))[0]
        strAsTuple = tuple(strAsList)
        obj = Covid19CSV(strAsTuple[1], strAsTuple[0], '')

        hdrAsTuple = tuple(hdr_.split(','))
        dateAsList = []
        for i in range(4, len(hdrAsTuple)):
            dateAsList.append(hdrAsTuple[i])
        valAsList = []
        for i in range(4, len(strAsTuple)):
            valAsList.append(strAsTuple[i])
        obj.setDate2Value(dateAsList, tuple(valAsList))
        # print(str(obj))
        return obj


    def setUp(self):
        self._header = "Province/State,Country/Region,Lat,Long,1/22/20,1/23/20,1/24/20,1/25/20,1/26/20,1/27/20,1/28/20,1/29/20,1/30/20,1/31/20,2/1/20,2/2/20,2/3/20,2/4/20,2/5/20,2/6/20,2/7/20,2/8/20,2/9/20,2/10/20,2/11/20,2/12/20,2/13/20,2/14/20,2/15/20,2/16/20,2/17/20,2/18/20,2/19/20,2/20/20,2/21/20,2/22/20,2/23/20,2/24/20,2/25/20,2/26/20,2/27/20,2/28/20,2/29/20,3/1/20,3/2/20,3/3/20,3/4/20,3/5/20,3/6/20,3/7/20,3/8/20,3/9/20,3/10/20,3/11/20,3/12/20,3/13/20,3/14/20,3/15/20,3/16/20,3/17/20,3/18/20,3/19/20,3/20/20,3/21/20,3/22/20,3/23/20,3/24/20,3/25/20,3/26/20,3/27/20,3/28/20,3/29/20,3/30/20,3/31/20,4/1/20,4/2/20,4/3/20,4/4/20,4/5/20,4/6/20,4/7/20,4/8/20"
        self._inputListFromFile = [
            ', Afghanistan, 33, 65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 5, 7, 7, 7, 11, 16, 21, 22, 22, 22, 24, 24, 40, 40, 74, 84, 94, 110, 110, 120, 170, 174, 237, 273, 281, 299, 349, 367, 423, 444',
            ', Albania, 41.1533, 20.1683, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 10, 12, 23, 33, 38, 42, 51, 55, 59, 64, 70, 76, 89, 104, 123, 146, 174, 186, 197, 212, 223, 243, 259, 277, 304, 333, 361, 377, 383, 400',
            ', Algeria, 28.0339, 1.6596, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 3, 5, 12, 12, 17, 17, 19, 20, 20, 20, 24, 26, 37, 48, 54, 60, 74, 87, 90, 139, 201, 230, 264, 302, 367, 409, 454, 511, 584, 716, 847, 986, 1171, 1251, 1320, 1423, 1468, 1572,'
            ', Andorra, 42.5063, 1.5218, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 39, 39, 53, 75, 88, 113, 133, 164, 188, 224, 267, 308, 334, 370, 376, 390, 428, 439, 466, 501, 525, 545, 564',
            ', Angola, -11.2027, 17.8739, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 7, 7, 8, 8, 8, 10, 14, 16, 17, 19',
            'Australian Capital Territory, Australia, -35.4735, 149.0124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 4, 6, 9, 19, 32, 39, 39, 53, 62, 71, 77, 78, 80, 84, 87, 91, 93, 96, 96, 96, 99',
            'New South Wales, Australia, -33.8688, 151.2093, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 6, 13, 22, 22, 26, 28, 38, 48, 55, 65, 65, 92, 112, 134, 171, 210, 267, 307, 353, 436, 669, 669, 818, 1029, 1219, 1405, 1617, 1791, 2032, 2032, 2182, 2298, 2389, 2493, 2580, 2637, 2686, 2734',
            'Northern Territory, Australia, -12.4634, 130.8456, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 5, 5, 6, 6, 12, 12, 15, 15, 15, 17, 19, 21, 22, 26, 27, 28, 28, 28',
            'Queensland, Australia, -28.0167, 153.4, 0, 0, 0, 0, 0, 0, 0, 1, 3, 2, 3, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9, 9, 9, 11, 11, 13, 13, 13, 15, 15, 18, 20, 20, 35, 46, 61, 68, 78, 94, 144, 184, 221, 259, 319, 397, 443, 493, 555, 625, 656, 689, 743, 781, 835, 873, 900, 907, 921, 934, 943',
            ', India, 21, 78, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 28, 30, 31, 34, 39, 43, 56, 62, 73, 82, 102, 113, 119, 142, 156, 194, 244, 330, 396, 499, 536, 657, 727, 887, 987, 1024, 1251, 1397, 1998, 2543, 2567, 3082, 3588, 4778, 5311, 5916',
            ', United Kingdom, 55.3781, -3.436, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 13, 13, 13, 15, 20, 23, 36, 40, 51, 85, 115, 163, 206, 273, 321, 382, 456, 456, 798, 1140, 1140, 1543, 1950, 2626, 2689, 3983, 5018, 5683, 6650, 8077, 9529, 11658, 14543, 17089, 19522, 22141, 25150, 29474, 33718, 38168, 41903, 47806, 51608, 55242, 60733'
            ]
        self._dateList = self._header.split(',')[4:]
        self._verificationObjects = []
        for l in self._inputListFromFile:
            self._verificationObjects.\
                append(TestCovid19GlobalTransformer._createVerificationObject(self._header, l))

    def test_colNamesICare(self):
        colList = ['Country/Region', 'Province/State']
        t1 = Covid19GlobalTransformer()
        self.assertEqual(colList, t1.listOfColumnNamesToRead())

    def test_lastColumnBeforeDates(self):
        t1 = Covid19GlobalTransformer()
        self.assertEqual('Long', t1.lastColNameBeforeDates())

    def test_process_header(self):
        def test1():
            t1 = Covid19GlobalTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader('')
            self.assertEqual(0, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))

        def test2():
            t1 = Covid19GlobalTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader([])
            self.assertEqual(0, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))

        def test3():
            t1 = Covid19GlobalTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader(['abc'])
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader(['Country/Region'])
            self.assertEqual(1, len(t1._colsToRead))
            t1.processHeader(['Country/Region', 'Province/State'])
            self.assertEqual(2, len(t1._colsToRead))
            t1.processHeader(['iso3', 'Country/Region', 'Province/State'])
            self.assertEqual(2, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))

        def test4():
            t1 = Covid19GlobalTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            # 'Province/State,Country/Region,Lat,Long,1/22/20,...'
            # 'Long' is index #3.
            t1.processHeader(self._header.split(',')[:3])
            self.assertEqual(2, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))
            # Include 'Long'.  'Long' is index #3.
            t1.processHeader(self._header.split(',')[:4])
            self.assertEqual(2, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))
            # # Include date after 'Long'.
            t1.processHeader(self._header.split(',')[:5])
            self.assertEqual(3, len(t1._colsToRead))
            self.assertEqual(1, len(t1._dateList))
            t1.processHeader(self._header.split(',')[:6])
            self.assertEqual(4, len(t1._colsToRead))
            self.assertEqual(2, len(t1._dateList))
            # All date columns.
            t1.processHeader(self._header.split(','))
            self.assertEqual(80, len(t1._colsToRead))
            self.assertEqual(78, len(t1._dateList))

        test1()
        test2()
        test3()
        test4()


    def test_columns_to_read(self):
        t1 = Covid19GlobalTransformer()
        colAsTuple = tuple(self._header.split(','))
        t1.processHeader(colAsTuple)
        self.assertEqual(0, len(t1._objColl))

        headerAsTuple = tuple(self._header.split(','))
        firstDatePos = headerAsTuple.index('Long') + 1
        self.assertTrue(firstDatePos > 1)
        numDateCols = len(headerAsTuple) - firstDatePos
        self.assertTrue(numDateCols > 0)

        l1 = t1.listOfIndexesOfColumnsToRead()
        self.assertEqual(numDateCols + len(t1.listOfColumnNamesToRead()), len(l1))
        self.assertEqual(0, len(t1._objColl))
        self.assertEqual(numDateCols, len(t1._dateList))

        l1AsTuple = tuple(l1)

        countryCol = headerAsTuple.index('Country/Region')
        self.assertTrue(countryCol >= 0)
        self.assertTrue(l1AsTuple.index(countryCol) >= 0)

        stateCol = headerAsTuple.index('Province/State')
        self.assertTrue(stateCol >= 0)
        self.assertTrue(l1AsTuple.index(stateCol) >= 0)

        # Check all date column header numbers are included.
        for i in range(firstDatePos, len(headerAsTuple)):
            self.assertTrue(l1AsTuple.index(i) >= 0)

        self.assertEqual(tuple(self._dateList), tuple(t1._dateList))


    @staticmethod
    def _createListFromCSVLine(str_):
        # Fields may have commas embedded.  Cannot use split.
        # For 'US, 31.12, -87.15, "Escambia, Alabama, US", 1/22/2020'
        return list(csv.reader([str_], delimiter=',', quotechar='"', skipinitialspace=True))[0]


    def test_create_object(self):
        t1 = Covid19GlobalTransformer()
        headerAsTuple = tuple(self._header.split(','))
        firstDatePos = headerAsTuple.index('Long') + 1
        numDateCols = len(headerAsTuple) - firstDatePos
        t1.processHeader(self._header.split(','))
        colIndexList = t1.listOfIndexesOfColumnsToRead()
        self.assertEqual(numDateCols + len(t1.listOfColumnNamesToRead()), len(colIndexList))

        for i in range(0, len(self._inputListFromFile)):
            line = self._inputListFromFile[i]
            lineAsList = TestCovid19GlobalTransformer._createListFromCSVLine(line)
            # print("xx = ", str(lineAsList))
            rawDataList = []
            for colIndex in colIndexList:
                rawDataList.append(lineAsList[colIndex])

            # print(str(tuple(rawDataList)))
            o1 = t1.createObject(tuple(rawDataList))
            self.assertIsNotNone(o1)
            self.assertEqual(str(self._verificationObjects[i]), str(o1))

            i = i + 1

    def test_add_to_collection(self):
        t1 = Covid19GlobalTransformer()
        self.assertEqual(0, len(t1._objColl))
        t1.processHeader(self._header.split(','))
        colList = t1.listOfIndexesOfColumnsToRead()

        for line in self._inputListFromFile:
            lineAsList = TestCovid19GlobalTransformer._createListFromCSVLine(line)
            rawDataList = []
            for col in colList:
                rawDataList.append(lineAsList[col])
            t1.addToCollection(t1.createObject(tuple(rawDataList)))
        self.assertEqual(len(self._inputListFromFile), len(t1._objColl))

        i = 0
        for obj in t1._objColl:
            self.assertEqual(str(self._verificationObjects[i]), str(obj))
            i = i + 1


    def test_get_collection(self):
        t1 = Covid19GlobalTransformer()
        self.assertEqual(0, len(t1._objColl))
        t1.processHeader(self._header.split(','))
        colList = t1.listOfIndexesOfColumnsToRead()

        for line in self._inputListFromFile:
            lineAsList = TestCovid19GlobalTransformer._createListFromCSVLine(line)
            rawDataList = []
            for col in colList:
                rawDataList.append(lineAsList[col])
            t1.addToCollection(t1.createObject(tuple(rawDataList)))

        self.assertEqual(len(self._verificationObjects), len(t1.getCollection()))
        i = 0
        for obj in t1.getCollection():
            self.assertEqual(str(self._verificationObjects[i]), str(obj))
            i = i + 1

    def test_process_line(self):
        t1 = Covid19GlobalTransformer()

        self.assertEqual(0, len(t1._colsToRead))
        self.assertEqual(0, len(t1._dateList))
        self.assertEqual(0, len(t1._objColl))
        t1.processLine(self._header.split(','), True)
        self.assertEqual(80, len(t1._colsToRead))
        self.assertEqual(78, len(t1._dateList))
        self.assertEqual(0, len(t1._objColl))

        for line in self._inputListFromFile:
            lineAsList = TestCovid19GlobalTransformer._createListFromCSVLine(line)
            t1.processLine(lineAsList, False)
        self.assertEqual(80, len(t1._colsToRead))
        self.assertEqual(78, len(t1._dateList))
        self.assertEqual(len(self._inputListFromFile), len(t1._objColl))

        i = 0
        for obj in t1.getCollection():
            self.assertEqual(str(self._verificationObjects[i]), str(obj))
            # print('{0}: {1}'.format(i, str(obj)))
            i = i + 1
        self.assertEqual(80, len(t1._colsToRead))
        self.assertEqual(78, len(t1._dateList))
        self.assertEqual(len(self._inputListFromFile), len(t1._objColl))

