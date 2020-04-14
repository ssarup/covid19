from transform.Covid19CSV import Covid19CSV
from transform.Covid19Transformer import Covid19Transformer


class Covid19USTransformer(Covid19Transformer):
    def __init__(self):
        super().__init__()

    def listOfColumnNamesToRead(self):
        return ['iso3', 'Province_State', 'Admin2']

    def lastColNameBeforeDates(self):
        return 'Combined_Key'

    def createObject(self, colsAsTuple_):
        obj1 = Covid19CSV(colsAsTuple_[0], colsAsTuple_[1], colsAsTuple_[2])
        obj1.setDate2Value(self._dateList, colsAsTuple_[3:])
        return obj1
