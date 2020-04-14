from abc import abstractmethod
from covid19io.AbsTransformer import AbsTransformer


class AbsTransformerWithHeader(AbsTransformer):
    """
    TODO: Remove header processing from AbsTransformer.
    """
    @abstractmethod
    def processHeader(self, colsAsTuple_):
        """
        Special processing for first line, assuming it could be a header
        :param colsAsTuple_: list of header columns
        :return: None
        """
        pass

    def processLine(self, lineList_, isFirstLine_):
        assert isinstance(isFirstLine_, bool)
        if isFirstLine_:
            self.processHeader(lineList_)
        else:
            impColumnList = []
            for col in self.listOfIndexesOfColumnsToRead():
                impColumnList.append(lineList_[col])
            obj = self.createObject(tuple(impColumnList))
            self.addToCollection(obj)
