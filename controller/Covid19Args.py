import argparse
import csv
from datetime import datetime
from constants.Covid19Constants import Covid19Constants
from controller.InputFileFactory import InputFileFactory


class Covid19Args(object):
    def __init__(self):
        self._parser = None
        self._inputfile = None
        self._globalInputfile = None
        self._download = False
        self._locationList = None
        self._templateOutputFile = None
        self._outputfile = None

    @staticmethod
    def _getLocationArgs(locStr_):

        def isValid(str_):
            # print('xx', str_, type(str_))
            # Should have / in str_.
            # Should not begin with /.
            # Can end with /.
            # USA/New Jersey/Middlesex is valid.
            # So is India//.
            # But must have at least two /.
            return str_.count('/') >= 2 and '/' != str_.strip()[0]

        locReader = csv.reader([locStr_], delimiter=',', quotechar='"', skipinitialspace=True)
        # locReader is of type csv._reader.
        # print(locStr_, str([locStr_]), str(locReader), type(locReader))
        return list(filter(isValid, list(locReader)[0]))

    @staticmethod
    def downloadFilenamesWithPath(timeSuffix=None):
        """
        Returns separate filenames for the following keys -
          1. US
          2. Global
        :param timeSuffix: Useful for testing. Will use system time if timeSuffix is None.
        :return: Hash table keyed on InputFileType.
        """
        today = datetime.today()
        if timeSuffix is None:
            timeSuffix = today.strftime('%H%M')

        fileType2NameWithPath = {}
        for fileType in InputFileFactory:
            filename = '{0}_{1}{2}.csv'.format(fileType.downloadFilePrefix(),
                                               today.strftime('%Y%m%d'), timeSuffix)
            fileWithPath = '{0}/{1}'.format(Covid19Constants.DOWNLOAD_FOLDER, filename)
            fileType2NameWithPath[fileType] = fileWithPath
        return fileType2NameWithPath

    @property
    def inputfile(self):
        return self._inputfile

    @property
    def globalInputfile(self):
        return self._globalInputfile

    @property
    def download(self):
        return self._download

    @property
    def locationList(self):
        return self._locationList

    @property
    def templateOutput(self):
        return self._templateOutputFile

    @property
    def outputfile(self):
        return self._outputfile

    def setup(self):
        self._parser = argparse.ArgumentParser(description='Covid19 analytics.')
        self._parser.add_argument('--input', type=str,
                                  help='name of input file')
        self._parser.add_argument('--globalInput', type=str,
                                  help='name of input file for global data')
        self._parser.add_argument('--download', action='store_true',
                                  help='download the file from the web')
        self._parser.add_argument('--location', type=str, required=True,
                                  help='comma-separated location as Country/State/County or State/County')
        self._parser.add_argument('--templateOutput', type=str, required=True,
                                  help='name of template Excel to use for output file')
        self._parser.add_argument('--output', type=str, required=True,
                                  help='name of output file')

    def parse(self, testList_=None):
        # testList_ is used for testing.
        if testList_ is None:
            args = self._parser.parse_args()
        else:
            args = self._parser.parse_args(testList_)
        self._inputfile = args.input
        self._globalInputfile = args.globalInput
        self._download = args.download
        self._locationList = Covid19Args._getLocationArgs(args.location)
        self._templateOutputFile = args.templateOutput
        self._outputfile = args.output
