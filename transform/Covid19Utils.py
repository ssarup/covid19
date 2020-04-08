from transform.Covid19CSVTransformer import Covid19CSV
from data.ObsCollection import ObsCollection
from data.Location import Location
from data.ObservationDate import ObservationDate


class Covid19Utils(object):

    @staticmethod
    def addCSVToObsCollection(csvObj_, obsColl_):
        """
        Convert a csvObj_ to an Observation, and add to collection of observations.
        :param csvObj_: Covid19CSV object
        :param obsColl_: Collection of observations as ObsCollection
        :return: List of Observation
        """
        assert isinstance(csvObj_, Covid19CSV)
        assert isinstance(obsColl_, ObsCollection)

        loc = Location(csvObj_.country, csvObj_.state, csvObj_.county)
        for dtStr in csvObj_.dateList:
            obsDate = ObservationDate.fromMDY(dtStr)
            if obsDate is None:
                # Try using the 2-digit year format, since the file can have either.
                obsDate = ObservationDate.fromMDY2(dtStr)
            # print(dtStr)
            assert isinstance(obsDate, ObservationDate)
            obsColl_.addObservation(loc, obsDate, csvObj_.date2Value[dtStr])


