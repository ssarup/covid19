from unittest import TestCase
import csv
from transform.Covid19USTransformer import Covid19USTransformer
from transform.Covid19CSV import Covid19CSV


class TestCovid19USTransformer(TestCase):
    @staticmethod
    def _createVerificationObject(hdr_, str_):
        # Input string may have embedded commas in a field.
        # 'aaa, bbb, "ccc, ddd", eee'
        strAsList = list(csv.reader([str_], delimiter=',', quotechar='"', skipinitialspace=True))[0]
        strAsTuple = tuple(strAsList)
        obj = Covid19CSV(strAsTuple[2], strAsTuple[6], strAsTuple[5])

        hdrAsTuple = tuple(hdr_.split(','))
        dateAsList = []
        for i in range(11, len(hdrAsTuple)):
            dateAsList.append(hdrAsTuple[i])
        valAsList = []
        for i in range(11, len(strAsTuple)):
            valAsList.append(strAsTuple[i])
        obj.setDate2Value(dateAsList, tuple(valAsList))
        # print(str(obj))
        return obj


    def setUp(self):
        self._header = "UID,iso2,iso3,code3,FIPS,Admin2,Province_State,Country_Region,Lat,Long_,Combined_Key,1/22/2020,1/23/2020,1/24/2020,1/25/2020,1/26/2020,1/27/2020,1/28/2020,1/29/2020,1/30/2020,1/31/2020,2/1/2020,2/2/2020,2/3/2020,2/4/2020,2/5/2020,2/6/2020,2/7/2020,2/8/2020,2/9/2020,2/10/2020,2/11/2020,2/12/2020,2/13/2020,2/14/2020,2/15/2020,2/16/2020,2/17/2020,2/18/2020,2/19/2020,2/20/2020,2/21/2020,2/22/2020,2/23/2020,2/24/2020,2/25/2020,2/26/2020,2/27/2020,2/28/2020,2/29/2020,3/1/2020,3/2/2020,3/3/2020,3/4/2020,3/5/2020,3/6/2020,3/7/2020,3/8/2020,3/9/2020,3/10/2020,3/11/2020,3/12/2020,3/13/2020,3/14/2020,3/15/2020,3/16/2020,3/17/2020,3/18/2020,3/19/2020,3/20/2020,3/21/2020,3/22/2020,3/23/2020,3/24/2020,3/25/2020,3/26/2020,3/27/2020,3/28/2020,3/29/2020,3/30/2020"
        self._inputListFromFile = [
            '84001053, US, USA, 840, 1053, Escambia, Alabama, US, 31.1256789, -87.15918694, "Escambia, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1',
            '84001055, US, USA, 840, 1055, Etowah, Alabama, US, 34.04567266, -86.04051873, "Etowah, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 6, 6, 6',
            '84001057, US, USA, 840, 1057, Fayette, Alabama, US, 33.72076938, -87.73886638, "Fayette, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1',
            '84001059, US, USA, 840, 1059, Franklin, Alabama, US, 34.44235334, -87.84289505, "Franklin, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 3',
            '84001061, US, USA, 840, 1061, Geneva, Alabama, US, 31.09389027, -85.83572839, "Geneva, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0',
            '84001063, US, USA, 840, 1063, Greene, Alabama, US, 32.85504247, -87.95684022, "Greene, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3',
            '84001065, US, USA, 840, 1065, Hale, Alabama, US, 32.76039258, -87.63284988, "Hale, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1',
            '84001067, US, USA, 840, 1067, Henry, Alabama, US, 31.51148016, -85.24267944, "Henry, Alabama, US", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0',
            '84005025,US,USA,840,5025,Cleveland,Arkansas,US,33.89723187,-92.18537045,"Cleveland, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,5,5,5',
            '84005027,US,USA,840,5027,Columbia,Arkansas,US,33.21230701,-93.22642793,"Columbia, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1',
            '84005029,US,USA,840,5029,Conway,Arkansas,US,35.26205537,-92.70506566,"Conway, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1',
            '84005031,US,USA,840,5031,Craighead,Arkansas,US,35.83018283,-90.63235729,"Craighead, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,6,6',
            '84005033,US,USA,840,5033,Crawford,Arkansas,US,35.58928601,-94.2446814,"Crawford, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1',
            '84005035,US,USA,840,5035,Crittenden,Arkansas,US,35.21247318,-90.30839406,"Crittenden, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,6,7,9,14,17,17',
            '84005037,US,USA,840,5037,Cross,Arkansas,US,35.29631396,-90.77185818,"Cross, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1',
            '84005039,US,USA,840,5039,Dallas,Arkansas,US,33.97042763,-92.65167437,"Dallas, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005041,US,USA,840,5041,Desha,Arkansas,US,33.83011025,-91.25500948,"Desha, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2',
            '84005043,US,USA,840,5043,Drew,Arkansas,US,33.59035001,-91.71777921,"Drew, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1',
            '84005045,US,USA,840,5045,Faulkner,Arkansas,US,35.14719007,-92.33717519,"Faulkner, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,10,14,23,24,27,29,30,30',
            '84005047,US,USA,840,5047,Franklin,Arkansas,US,35.51202821,-93.89299569,"Franklin, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005049,US,USA,840,5049,Fulton,Arkansas,US,36.38177105,-91.81729127,"Fulton, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005051,US,USA,840,5051,Garland,Arkansas,US,34.57692074,-93.14921604,"Garland, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,9,10,16,18,20,20,25,26',
            '84005053,US,USA,840,5053,Grant,Arkansas,US,34.29017991,-92.42320562,"Grant, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,3,3,3',
            '84005055,US,USA,840,5055,Greene,Arkansas,US,36.1173546,-90.55832668,"Greene, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1',
            '84005057,US,USA,840,5057,Hempstead,Arkansas,US,33.73325583,-93.66935133,"Hempstead, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1',
            '84005059,US,USA,840,5059,Hot Spring,Arkansas,US,34.31709259,-92.95396325,"Hot Spring, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1',
            '84005061,US,USA,840,5061,Howard,Arkansas,US,34.09007427,-93.9934871,"Howard, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1',
            '84005063,US,USA,840,5063,Independence,Arkansas,US,35.74242707,-91.57001641,"Independence, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,3,3,3',
            '84005065,US,USA,840,5065,Izard,Arkansas,US,36.09604046,-91.90847954,"Izard, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005067,US,USA,840,5067,Jackson,Arkansas,US,35.59802983,-91.21494602,"Jackson, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005069,US,USA,840,5069,Jefferson,Arkansas,US,34.26767081,-91.92619839,"Jefferson, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,9,21,21,22,23,23,25,25,26',
            '84005071,US,USA,840,5071,Johnson,Arkansas,US,35.56759135,-93.46036368,"Johnson, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1',
            '84005073,US,USA,840,5073,Lafayette,Arkansas,US,33.24116713,-93.60677071,"Lafayette, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005075,US,USA,840,5075,Lawrence,Arkansas,US,36.04188196,-91.10867198,"Lawrence, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1',
            '84005077,US,USA,840,5077,Lee,Arkansas,US,34.78498904,-90.78383866,"Lee, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005079,US,USA,840,5079,Lincoln,Arkansas,US,33.95317155,-91.74002806,"Lincoln, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,5,5,6,6,6',
            '84005081,US,USA,840,5081,Little River,Arkansas,US,33.70375665,-94.23468591,"Little River, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005083,US,USA,840,5083,Logan,Arkansas,US,35.21413234,-93.71951016,"Logan, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005085,US,USA,840,5085,Lonoke,Arkansas,US,34.75392199,-91.88742357,"Lonoke, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1',
            '84005087,US,USA,840,5087,Madison,Arkansas,US,36.01038185,-93.72524943,"Madison, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005089,US,USA,840,5089,Marion,Arkansas,US,36.26844485,-92.68451899,"Marion, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005091,US,USA,840,5091,Miller,Arkansas,US,33.31403423,-93.89285258,"Miller, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005093,US,USA,840,5093,Mississippi,Arkansas,US,35.76271485,-90.0519437,"Mississippi, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005095,US,USA,840,5095,Monroe,Arkansas,US,34.6815935,-91.20540287,"Monroe, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005097,US,USA,840,5097,Montgomery,Arkansas,US,34.53704874,-93.65824478,"Montgomery, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005099,US,USA,840,5099,Nevada,Arkansas,US,33.66340119,-93.30632432,"Nevada, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1',
            '84005101,US,USA,840,5101,Newton,Arkansas,US,35.91947491,-93.21612969,"Newton, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005103,US,USA,840,5103,Ouachita,Arkansas,US,33.58839816,-92.87795984,"Ouachita, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005105,US,USA,840,5105,Perry,Arkansas,US,34.9459153,-92.94372564,"Perry, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1',
            '84005107,US,USA,840,5107,Phillips,Arkansas,US,34.43268455,-90.84800154,"Phillips, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005109,US,USA,840,5109,Pike,Arkansas,US,34.16250414,-93.65789349,"Pike, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1',
            '84005111,US,USA,840,5111,Poinsett,Arkansas,US,35.57433534,-90.66268713,"Poinsett, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,3,3,3',
            '84005113,US,USA,840,5113,Polk,Arkansas,US,34.48254879,-94.22728802,"Polk, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1',
            '84005115,US,USA,840,5115,Pope,Arkansas,US,35.44871474,-93.03212219,"Pope, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1',
            '84005117,US,USA,840,5117,Prairie,Arkansas,US,34.83624419,-91.55162157,"Prairie, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005119,US,USA,840,5119,Pulaski,Arkansas,US,34.77054088,-92.31355101,"Pulaski, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,61,64,78,83,88,92,93,94',
            '84005121,US,USA,840,5121,Randolph,Arkansas,US,36.3415714,-91.02455531,"Randolph, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1',
            '84005123,US,USA,840,5123,St. Francis,Arkansas,US,35.02201976,-90.74828138,"St. Francis, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005125,US,USA,840,5125,Saline,Arkansas,US,34.64916145,-92.67583224,"Saline, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,4,4,4,4,4,6,6',
            '84005127,US,USA,840,5127,Scott,Arkansas,US,34.85588887,-94.0632176,"Scott, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0',
            '84005129,US,USA,840,5129,Searcy,Arkansas,US,35.9109364,-92.69936482,"Searcy, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2',
            '84005131,US,USA,840,5131,Sebastian,Arkansas,US,35.19605503,-94.27162713,"Sebastian, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,5',
            '84005133,US,USA,840,5133,Sevier,Arkansas,US,33.99780401,-94.2424869,"Sevier, Arkansas, US",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1'
        ]

        self._dateList = self._header.split(',')[11:]
        self._verificationObjects = []
        for l in self._inputListFromFile:
            self._verificationObjects.\
                append(TestCovid19USTransformer._createVerificationObject(self._header, l))


    def test_process_header(self):
        def test1():
            t1 = Covid19USTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader('')
            self.assertEqual(0, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))

        def test2():
            t1 = Covid19USTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader([])
            self.assertEqual(0, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))

        def test3():
            t1 = Covid19USTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader(['abc'])
            self.assertEqual(0, len(t1._colsToRead))
            t1.processHeader(['iso3'])
            self.assertEqual(1, len(t1._colsToRead))
            t1.processHeader(['iso3', 'Province_State'])
            self.assertEqual(2, len(t1._colsToRead))
            t1.processHeader(['iso3', 'Province_State', 'abracadabra'])
            self.assertEqual(2, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))

        def test4():
            t1 = Covid19USTransformer()
            self.assertEqual(0, len(t1._colsToRead))
            # '"UID,iso2,iso3,code3,FIPS,Admin2,Province_State,Country_Region,Lat,Long_,Combined_Key,1/22/2020...'
            # Before 'Combined_Key'.  'Combined_Key' is index #10.
            t1.processHeader(self._header.split(',')[:10])
            self.assertEqual(3, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))
            # Include 'Combined_Key'.  'Combined_Key' is index #10.
            t1.processHeader(self._header.split(',')[:11])
            self.assertEqual(3, len(t1._colsToRead))
            self.assertEqual(0, len(t1._dateList))
            # # Include date after 'Combined_Key'.
            t1.processHeader(self._header.split(',')[:12])
            self.assertEqual(4, len(t1._colsToRead))
            self.assertEqual(1, len(t1._dateList))
            t1.processHeader(self._header.split(',')[:13])
            self.assertEqual(5, len(t1._colsToRead))
            self.assertEqual(2, len(t1._dateList))
            # All date columns.
            t1.processHeader(self._header.split(','))
            self.assertEqual(72, len(t1._colsToRead))
            self.assertEqual(69, len(t1._dateList))

        test1()
        test2()
        test3()
        test4()


    def test_columns_to_read(self):
        t1 = Covid19USTransformer()
        colAsTuple = tuple(self._header.split(','))
        t1.processHeader(colAsTuple)
        self.assertEqual(0, len(t1._objColl))

        headerAsTuple = tuple(self._header.split(','))
        firstDatePos = headerAsTuple.index('Combined_Key') + 1
        self.assertTrue(firstDatePos > 1)
        numDateCols = len(headerAsTuple) - firstDatePos
        self.assertTrue(numDateCols > 0)

        l1 = t1.columnsToRead()
        self.assertEqual(numDateCols + 3, len(l1))
        self.assertEqual(0, len(t1._objColl))
        self.assertEqual(numDateCols, len(t1._dateList))

        l1AsTuple = tuple(l1)

        countryCol = headerAsTuple.index('iso3')
        self.assertTrue(countryCol > 0)
        self.assertTrue(l1AsTuple.index(countryCol) >= 0)

        stateCol = headerAsTuple.index('Province_State')
        self.assertTrue(stateCol > 0)
        self.assertTrue(l1AsTuple.index(stateCol) >= 0)

        countyCol = headerAsTuple.index('Admin2')
        self.assertTrue(countyCol > 0)
        self.assertTrue(l1AsTuple.index(countyCol) >= 0)

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
        t1 = Covid19USTransformer()
        headerAsTuple = tuple(self._header.split(','))
        firstDatePos = headerAsTuple.index('Combined_Key') + 1
        numDateCols = len(headerAsTuple) - firstDatePos
        t1.processHeader(self._header.split(','))
        colList = t1.columnsToRead()
        self.assertEqual(numDateCols + 3, len(colList))

        for i in range(0, len(self._inputListFromFile)):
            line = self._inputListFromFile[i]
            lineAsList = TestCovid19USTransformer._createListFromCSVLine(line)
            # print("xx = ", str(lineAsList))
            rawDataList = []
            for col in colList:
                rawDataList.append(lineAsList[col])

            # print(str(tuple(rawDataList)))
            o1 = t1.createObject(tuple(rawDataList))
            self.assertIsNotNone(o1)
            self.assertEqual(str(self._verificationObjects[i]), str(o1))

            i = i + 1

    def test_add_to_collection(self):
        t1 = Covid19USTransformer()
        self.assertEqual(0, len(t1._objColl))
        t1.processHeader(self._header.split(','))
        colList = t1.columnsToRead()

        for line in self._inputListFromFile:
            lineAsList = TestCovid19USTransformer._createListFromCSVLine(line)
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
        t1 = Covid19USTransformer()
        self.assertEqual(0, len(t1._objColl))
        t1.processHeader(self._header.split(','))
        colList = t1.columnsToRead()

        for line in self._inputListFromFile:
            lineAsList = TestCovid19USTransformer._createListFromCSVLine(line)
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
        t1 = Covid19USTransformer()

        self.assertEqual(0, len(t1._colsToRead))
        self.assertEqual(0, len(t1._dateList))
        self.assertEqual(0, len(t1._objColl))
        t1.processLine(self._header.split(','), True)
        self.assertEqual(72, len(t1._colsToRead))
        self.assertEqual(69, len(t1._dateList))
        self.assertEqual(0, len(t1._objColl))

        for line in self._inputListFromFile:
            lineAsList = TestCovid19USTransformer._createListFromCSVLine(line)
            t1.processLine(lineAsList, False)
        self.assertEqual(72, len(t1._colsToRead))
        self.assertEqual(69, len(t1._dateList))
        self.assertEqual(len(self._inputListFromFile), len(t1._objColl))

        i = 0
        for obj in t1.getCollection():
            self.assertEqual(str(self._verificationObjects[i]), str(obj))
            # print('{0}: {1}'.format(i, str(obj)))
            i = i + 1
        self.assertEqual(72, len(t1._colsToRead))
        self.assertEqual(69, len(t1._dateList))
        self.assertEqual(len(self._inputListFromFile), len(t1._objColl))

