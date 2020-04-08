from unittest import TestCase
from datetime import datetime
from transform.Covid19CSVTransformer import Covid19CSV
from transform.Covid19Utils import Covid19Utils
from data.ObsCollection import ObsCollection
from data.Location import Location


class TestCovid19Utils(TestCase):
    def test_add_csvto_obs_collection(self):
        def createLoc(s1_, s2_, s3_):
            return Location(country_=s1_, state_=s2_, county_=s3_)

        def test1():
            cObj = Covid19CSV('aa', 'bb', 'cc')
            oColl = ObsCollection()
            Covid19Utils.addCSVToObsCollection(cObj, oColl)
            self.assertEqual(0, oColl.numObservations())
            self.assertEqual(0, len(oColl.locations()))

        def test2():
            cObj = Covid19CSV('aa', 'bb', 'cc')
            cObj.setDate2Value(['1/1/2020'], (10,))
            oColl = ObsCollection()
            Covid19Utils.addCSVToObsCollection(cObj, oColl)
            self.assertEqual(1, oColl.numObservations())
            self.assertEqual(1, len(oColl.locations()))
            locations = list(oColl.locations())
            self.assertEqual('aa', locations[0]._country)
            self.assertEqual('bb', locations[0]._state)
            self.assertEqual('cc', locations[0]._county)
            obsList = oColl.getObservations(locations[0])
            self.assertEqual(1, len(obsList))
            self.assertEqual(datetime.strptime('1/1/2020', '%m/%d/%Y'), obsList[0]._obsDate._value)
            self.assertEqual(10, obsList[0]._value)

        def test3():
            cObj = Covid19CSV('aa', 'bb', 'cc')
            cObj.setDate2Value(['1/1/20'], (10,))
            oColl = ObsCollection()
            Covid19Utils.addCSVToObsCollection(cObj, oColl)
            self.assertEqual(1, oColl.numObservations())
            self.assertEqual(1, len(oColl.locations()))
            locations = list(oColl.locations())
            self.assertEqual('aa', locations[0]._country)
            self.assertEqual('bb', locations[0]._state)
            self.assertEqual('cc', locations[0]._county)
            obsList = oColl.getObservations(locations[0])
            self.assertEqual(1, len(obsList))
            self.assertEqual(datetime.strptime('1/1/2020', '%m/%d/%Y'), obsList[0]._obsDate._value)
            self.assertEqual(10, obsList[0]._value)

        def test4():
            locList = [
                ('aa', 'bb', 'cc'),
                ('aa', 'bb', 'dd'),
                ('aa', 'ee', 'cc'),
                ('ff', 'bb', 'cc')
            ]
            dateList = [
                ('1/1/2020', '1/2/2020', '1/3/2020', '1/4/2020'),
                ('1/1/2020', '1/5/2020'),
                ('1/6/2020',),
                ('1/7/2020',)
            ]
            valueList = [
                (10, 20, 30, 40),
                (100, 200),
                (3000,),
                (45,)
            ]
            numObservations = [4, 2, 1, 1]

            def setup(obsColl_):
                i = 0
                for item in locList:
                    covidObj = Covid19CSV(item[0], item[1], item[2])
                    dates = list(dateList[i])
                    values = valueList[i]
                    covidObj.setDate2Value(dates, values)
                    Covid19Utils.addCSVToObsCollection(covidObj, obsColl_)
                    i = i + 1

            def verifyObs(obsColl_):
                def compareLists(dateTup_, valueTup_, obsL_):
                    j = 0
                    self.assertEqual(len(dateTup_), len(valueTup_))
                    for dtStr in dateTup_:
                        # print(dtStr, valueTup_[j])
                        dt = datetime.strptime(dtStr, '%m/%d/%Y')
                        value = valueTup_[j]
                        obs = obsL_[j]
                        # print(str(obs))
                        self.assertEqual(dt, obs._obsDate._value)
                        self.assertEqual(value, obs._value)
                        j = j + 1

                i = 0
                for locTup in locList:
                    loc = Location(country_=locTup[0], state_=locTup[1], county_=locTup[2])
                    obsList = obsColl_.getObservations(loc)
                    self.assertEqual(len(valueList[i]), len(obsList))
                    compareLists(dateList[i], valueList[i], obsList)
                    i = i + 1

            obsColl = ObsCollection()
            setup(obsColl)
            self.assertEqual(len(locList), len(obsColl.locations()))
            self.assertEqual(8, obsColl.numObservations())
            # print(str(obsColl))
            verifyObs(obsColl)

        test1()
        test2()
        test3()
        test4()
