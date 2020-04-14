from transform.Covid19CSV import Covid19CSV
from transform.Covid19Transformer import Covid19Transformer


class Covid19GlobalTransformer(Covid19Transformer):
    def __init__(self):
        super().__init__()

    def listOfColumnNamesToRead(self):
        return ['Country/Region', 'Province/State']

    def lastColNameBeforeDates(self):
        return 'Long'

    def createObject(self, colsAsTuple_):
        obj1 = Covid19CSV(colsAsTuple_[0], colsAsTuple_[1], '')
        obj1.setDate2Value(self._dateList, colsAsTuple_[2:])
        return obj1
