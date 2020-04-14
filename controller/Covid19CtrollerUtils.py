from controller.Covid19Args import Covid19Args
from controller.InputFileFactory import InputFileFactory
from covid19io.Covid19InputDownloader import Covid19InputDownloader
from covid19io.FileReader import FileReader
from data.ObsCollection import ObsCollection
from transform.Covid19TransformUtils import Covid19TransformUtils


class Covid19ControllerUtils(object):
    @staticmethod
    def setupInputsFromArgs(args_):
        """
        Takes in Covid19Args and returns a list of tuples.
        Tuple contains -
          1. Input Type
          2. File name with path.
        Note if args_ has 'download' set to True, no explicitly specified input files will be considered.
        :param args_: Covid19Args
        :return: List of tuples containing input type and file name.
        """
        assert isinstance(args_, Covid19Args)
        inputList = []
        if args_.download:
            # TODO downloadFilenamesWithPath is a static call.
            downloadFilenamesWithPath = Covid19Args.downloadFilenamesWithPath()
            for fileType in downloadFilenamesWithPath.keys():
                assert isinstance(fileType, InputFileFactory)
                inputfile = Covid19InputDownloader.downloadFile(fileType.downloadURL(),
                                                                downloadFilenamesWithPath[fileType])
                # Create tuple as InputFileType, filename.
                inputList.append((fileType, inputfile))
        else:
            # US Input file.
            if args_.inputfile is not None:
                inputList.append((InputFileFactory.CONFIRMED_US, args_.inputfile)),

            if args_.globalInputfile is not None:
                inputList.append((InputFileFactory.CONFIRMED_GLOBAL, args_.globalInputfile))

        return inputList


    @staticmethod
    def createObsCollection(inputList_):
        """
        Create a ObsCollection object based on a list of tuples.
        Each tuple in the list contains -
          1. The input type.
          2. The input file name.
        :param inputList_: List of tuples containing input type and file name.
        :return: ObsCollection object.
        """
        obsColl = ObsCollection()
        for item in inputList_:
            fileType = item[0]
            assert isinstance(fileType, InputFileFactory)
            print("\nProcessing type '{0}.".format(fileType.name))

            filename = item[1]
            print("Working on file '{0}'.".format(filename))
            rdr = FileReader(filename)

            tx = fileType.covid19Transformer()
            rdr.read(tx)
            print("Read {0} lines from file {1}.".format(len(tx.getCollection()), filename))

            for covid19Obj in tx.getCollection():
                Covid19TransformUtils.addCSVToObsCollection(covid19Obj, obsColl)
        return obsColl
