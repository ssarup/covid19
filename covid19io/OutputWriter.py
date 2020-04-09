from abc import abstractmethod


class OutputWriter(object):
    @abstractmethod
    def writeLine(self, tup_, header_):
        assert isinstance(header_, bool)
        pass
