from data.Location import Location
from data.ObsCollection import ObsCollection


class Covid19Outputter(object):
    def __init__(self, writer_):
        # assert isinstance(writer_, OutputWriter)
        self._writer = writer_

    def writeHeader(self):
        headerTup = tuple('Country', 'State', 'County', 'City', 'Date', 'Observation')
        self._writer.writeLine(headerTup, header_=True)

    def writeColl(self, loc_, obsColl_):
        assert isinstance(loc_, Location)
        assert isinstance(obsColl_, ObsCollection)
        for obs in obsColl_.getObservations(loc_):
            lineTup = tuple(loc_.countr, loc_.state, loc_.county, loc_.city, obs._obsDate._value, obs._value)
            self.writer.writeLine(lineTup, header_=False)
            # print('"{0}","{1}",{2},{3}'.format(loc.state,loc.county,obs._obsDate._value.strftime('%m/%d/%Y'), obs._value))

