from unittest import TestCase
from datetime import datetime, timedelta
from data.Location import Location
from data.ObservationDate import ObservationDate
from data.ObsCollection import ObsCollection
from data.Observation import Observation


class TestObsCollection(TestCase):

    @staticmethod
    def _makeKey(loc_, index_):
        return '{0}:{1}'.format(loc_, str(index_))

    def setUp(self):
        self._MULTIPLIER = 1000
        self._NUM_LOC = 10
        self._NUM_OBS = 7
        if self._NUM_OBS >= self._MULTIPLIER:
            raise Exception('Error: _NUM_OBJ cannot be more thank _MULTIPLIER.\nKey creation will fail!')

        self._inputs = []
        self._checkLoc = []
        self._checkDate = {}        # Key is Loc:index
        self._checkValues = {}      # Key is Loc:index

        dt = datetime.strptime('1/1/2020', '%m/%d/%Y')
        for i in range(0, self._NUM_LOC):
            loc = Location(str(i))
            self._checkLoc.append(loc)

            for j in range(0, self._NUM_OBS):
                value = i * self._MULTIPLIER + j
                keyIndex = value
                key = TestObsCollection._makeKey(loc, keyIndex)
                dtNow = dt + timedelta(days=keyIndex)
                self._inputs.append((loc, dtNow.strftime('%m/%d/%Y'), value))
                self._checkDate[key] = dtNow
                self._checkValues[key] = value

        self._numInputs = len(self._inputs)
        # print("inputs = " + str(self._numInputs))


    def test_num_observations(self):
        coll = ObsCollection()
        self.assertEqual(coll.numObservations(), 0)

        obsDate = lambda dt : ObservationDate.fromMDY(dt.strftime('%m/%d/%Y'))
        coll.addObservation(Location(city_="New City"), obsDate(datetime.now()), 1)
        self.assertEqual(coll.numObservations(), 1)


    def _addObservationHelper(self, numInputs_):
        coll = ObsCollection()

        for i in range(0, numInputs_):
            def makeObsDate(dtStr_):
                return ObservationDate.fromMDY(dtStr_)

            coll.addObservation(self._inputs[i][0], makeObsDate(self._inputs[i][1]), self._inputs[i][2])
            self.assertEqual(coll.numObservations(), i + 1)

        return coll


    def test_add_observation(self):
        coll = self._addObservationHelper(self._numInputs)
        self.assertEqual(coll.numObservations(), self._numInputs)


    def test_locations(self):
        coll = self._addObservationHelper(self._numInputs)
        locations = coll.locations()
        self.assertEqual(len(locations), self._NUM_LOC)
        # loc = locations[0]
        locSet = set(locations)
        # print(len(str(locSet)))
        inputLocSet = set(self._checkLoc)
        self.assertEqual(len(inputLocSet), self._NUM_LOC)
        self.assertEqual(len(locSet.intersection(inputLocSet)), self._NUM_LOC)
        self.assertEqual(len(locSet.union(inputLocSet)), self._NUM_LOC)


    def test_get_observations(self):
        coll = self._addObservationHelper(self._numInputs)
        self.assertEqual(coll.numObservations(), self._numInputs)

        def verifyObservation(loc_, obs_):
            assert isinstance(loc_, Location)
            assert isinstance(obs_, Observation)
            key = TestObsCollection._makeKey(loc_, obs_._value)
            self.assertEqual(obs_._obsDate._value, self._checkDate[key])
            self.assertEqual(obs_._value, self._checkValues[key])

        for loc in self._checkLoc:
            # print(str(loc))
            observations = coll.getObservations(loc)
            for obs in observations:
                # print("obs = {0}".format(str(obs)))
                verifyObservation(loc, obs)

    def test_headerForOutput(self):
        checkStr = "('Country', 'State', 'County', 'City', 'Date', 'Observation')"
        self.assertEqual(checkStr, str(ObsCollection.headerForOutput()))
        # print('('Country', 'State', 'County', 'City', 'Date', 'Observation'), str(ObsCollection.headerForOutput()))
