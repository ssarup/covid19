from data.Location import Location
from data.ObservationDate import ObservationDate
from data.Observation import Observation


class ObsCollection(object):
    def __init__(self):
        self._obs = []          # List of Observations.
        self._loc2Obs = {}      # Location to Observation array.

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

