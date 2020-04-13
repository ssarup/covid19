from abc import abstractmethod


class AbsTransformer(object):
    @abstractmethod
    def processHeader(self, headerColsList_):
        """
        Special processing for first line, assuming it could be a header.
        Can be used to setup the columns that need to be read.
        :param headerColsAsList_: list of header columns
        :return: None
        """
        pass

    @abstractmethod
    def listOfIndexesOfColumnsToRead(self):
        """
        Index number of columns to read from input file.
        :return: List of index numbers of columns to read
        """
        pass

    @abstractmethod
    def createObject(self, colsAsTuple_):
        """
        Create object from colAsTuple_
        :param colsAsTuple_: only the columns that are needed to create object.
        :return: created object.
        """
        pass

    @abstractmethod
    def addToCollection(self, obj_):
        """
        Add obj_ to internal collection.
        :param obj_: obj_ to add
        :return: None
        """
        pass

    @abstractmethod
    def getCollection(self):
        """
        Return internal collection as List.
        :return: internal collection of objects as List.
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
