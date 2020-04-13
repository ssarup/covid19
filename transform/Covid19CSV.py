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