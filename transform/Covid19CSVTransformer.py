from covid19io.AbsTransformer import AbsTransformer


class Covid19CSV(object):
    def __init__(self, country_, state_, county_):
        assert isinstance(country_, str)
        assert isinstance(state_, str)
        assert isinstance(county_, str)
        self._country = country_
        self._state = state_
        self._county = county_
        self._dateList = []
        self._date2Value = {}       # DateAsString '%m/%d/%Y' to Value

    def setDate2Value(self, dateList_, valueAsTuple_):
        i = 0
        self._dateList = []
        self._date2Value = {}       # DateAsString '%m/%d/%Y' to Value
        maxEntries = len(dateList_)
        if len(valueAsTuple_) < maxEntries:
            maxEntries = len(valueAsTuple_)
        self._dateList = dateList_[0:maxEntries]
        for dt in self._dateList:
            assert isinstance(dt, str)
            # Convert value to int.
            # TODO is there a way to make this more generic.
            self._date2Value[dt] = int(valueAsTuple_[i])
            # print('{0} = {1} -> {2}'.format(i, dt, valueAsTuple_[i]))
            i = i + 1

    def __str__(self):
        retVal = ['[country = ', self._country, ', state = ', self._state, ', county = ', self._county]
        for k in self._date2Value.keys():
            dateValOut = [', [']
            dateValOut.append(k)
            dateValOut.append(' -> ')
            dateValOut.append(str(self._date2Value[k]))
            dateValOut.append(']')
            retVal.append(''.join(dateValOut))
        retVal.append(']')
        return ''.join(retVal)

    @property
    def country(self):
        return self._country

    @property
    def state(self):
        return self._state

    @property
    def county(self):
        return self._county

    @property
    def dateList(self):
        return self._dateList

    @property
    def date2Value(self):
        return self._date2Value


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
