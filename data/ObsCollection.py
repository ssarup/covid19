from data.Location import Location
from data.ObservationDate import ObservationDate
from data.Observation import Observation


class ObsCollection(object):
    def __init__(self):
        self._obs = []          # List of Observations.
        self._loc2Obs = {}      # Location to Observation array.

    @staticmethod
    def headerForOutput():
        return ('Country', 'State', 'County', 'City', 'Date', 'Observation')

    def addObservation(self, loc_, date_, value_):
        assert isinstance(loc_, Location)
        assert isinstance(date_, ObservationDate)

        obs = Observation(date_, value_)
        self._obs.append(obs)

        # Check if no entry, create empty list.  Then append to existing list.
        self._loc2Obs.setdefault(loc_, []).append(obs)

    def numObservations(self):
        return len(self._obs)

    def locations(self):
        return self._loc2Obs.keys()

    def getObservations(self, loc_):
        assert isinstance(loc_, Location)
        if loc_ in self._loc2Obs.keys():
            return self._loc2Obs[loc_]
        else:
            return None

    def __str__(self):
        strList = ['[']
        for loc in self._loc2Obs.keys():
            strList.append('[{0} -> ['.format(str(loc)))
            for obs in self._loc2Obs[loc]:
                strList.append('({0}), '.format(str(obs)))
            strList.append('],\n')
        strList.append(']')
        return ''.join(strList)
