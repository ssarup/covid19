from covid19io.AbsTransformer import AbsTransformer
from transform.Covid19CSV import Covid19CSV


class Covid19CSVTransformer(AbsTransformer):
    def __init__(self):
        # self._headerAsStr = headerAsStr_
        self._COLS_I_CARE_LIST = ['iso3', 'Province_State', 'Admin2']
        self._colsToRead = []
        self._dateList = []
        self._objColl = []


    def processHeader(self, headerColsAsList_):
        self._colsToRead = []
        self._dateList = []
        headerAsTuple = tuple(headerColsAsList_)

        # Find index of interesting columns.
        for c in self._COLS_I_CARE_LIST:
            if c in headerAsTuple:
                self._colsToRead.append(headerAsTuple.index(c))
        # '"UID,iso2,iso3,code3,FIPS,Admin2,Province_State,Country_Region,Lat,Long_,Combined_Key,1/22/2020...'
        # Should have 2, 6, 5 at this point.

        # Find starting of date.  It is after the 'Combined_Key' column
        if 'Combined_Key' in headerAsTuple:
            firstPos = headerAsTuple.index('Combined_Key') + 1
            lastPos = len(headerAsTuple)
            # print('{0}, {1}'.format(firstPos, lastPos))
            for i in range(firstPos, lastPos):
                self._dateList.append(headerAsTuple[i])
                self._colsToRead.append(i)


    def columnsToRead(self):
        return self._colsToRead


    def createObject(self, colsAsTuple_):
        obj1 = Covid19CSV(colsAsTuple_[0], colsAsTuple_[1], colsAsTuple_[2])
        obj1.setDate2Value(self._dateList, colsAsTuple_[3:])
        return obj1


    def addToCollection(self, obj_):
        self._objColl.append(obj_)


    def getCollection(self):
        return self._objColl
