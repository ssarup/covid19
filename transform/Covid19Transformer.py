from abc import abstractmethod
from covid19io.AbsTransformer import AbsTransformer
from transform.Covid19CSV import Covid19CSV


class Covid19Transformer(AbsTransformer):
    def __init__(self):
        self._colsToRead = []
        self._dateList = []
        self._objColl = []

    @abstractmethod
    def listOfColumnNamesToRead(self):
        """
        Return list of columns I case from the input file
        :return: list of strings containing names of columns in input file.
        """
        pass

    @abstractmethod
    def lastColNameBeforeDates(self):
        """
        Name of the last column before dates start.
        :return: name of the last column name before start of dates.
        """
        pass

    def processHeader(self, headerColsAsList_):
        self._colsToRead = []
        self._dateList = []
        headerAsTuple = tuple(headerColsAsList_)

        # Find index of interesting columns.
        for c in self.listOfColumnNamesToRead():
            if c in headerAsTuple:
                self._colsToRead.append(headerAsTuple.index(c))
        # '"UID,iso2,iso3,code3,FIPS,Admin2,Province_State,Country_Region,Lat,Long_,Combined_Key,1/22/2020...'
        # Should have 2, 6, 5 at this point.

        # Find starting of date.  It is after the 'Combined_Key' column
        if self.lastColNameBeforeDates() in headerAsTuple:
            firstPos = headerAsTuple.index(self.lastColNameBeforeDates()) + 1
            lastPos = len(headerAsTuple)
            # print('{0}, {1}'.format(firstPos, lastPos))
            for i in range(firstPos, lastPos):
                self._dateList.append(headerAsTuple[i])
                self._colsToRead.append(i)


    def listOfIndexesOfColumnsToRead(self):
        return self._colsToRead


    def addToCollection(self, obj_):
        self._objColl.append(obj_)


    def getCollection(self):
        return self._objColl
