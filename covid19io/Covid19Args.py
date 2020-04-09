import argparse
import csv


class Covid19Args(object):
    def __init__(self):
        self._parser = None
        self._inputfile = None
        self._locationList = None
        self._templateOutputFile = None
        self._outputfile = None

    @staticmethod
    def _getLocationArgs(locStr_):

        def isValid(str_):
            # print('xx', str_, type(str_))
            # Should have / in str_.
            # Should not begin with /.
            # Should not end with /.
            return '/' in str_ and '/' != str_.strip()[0] and '/' != str_.strip()[-1]

        locReader = csv.reader([locStr_], delimiter=',', quotechar='"', skipinitialspace=True)
        # locReader is of type csv._reader.
        # print(locStr_, str([locStr_]), str(locReader), type(locReader))
        return list(filter(isValid, list(locReader)[0]))

    @property
    def inputfile(self):
        return self._inputfile

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
        self._parser.add_argument('--input', type=str, required=True,
                                  help='name of input file')
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
        self._locationList = Covid19Args._getLocationArgs(args.location)
        self._templateOutputFile = args.templateOutput
        self._outputfile = args.output
