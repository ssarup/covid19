import csv
from covid19io.AbsTransformer import AbsTransformer


class FileReader(object):
    def __init__(self, name_):
        self._fName = name_
        self._fHandle = None

    def read(self, transformer_):
        assert isinstance(transformer_, AbsTransformer)
        isFirstLine = True
        try:
            self._fHandle = open(self._fName)
            rdr = csv.reader(self._fHandle, delimiter=',', quotechar='"', skipinitialspace=True)
            # delimiter and quotechar to handle comma between quoted strings.
            # skipinitialspace ensures that the space after comma is excluded.
            # input str = ''aaa, bbb, "ccc, ddd"'
            # output should be like ['aaa', 'bbb', 'ccc, ddd']

            for row in rdr:
                transformer_.processLine(row, isFirstLine)
                isFirstLine = False
        finally:
            if self._fHandle is not None:
                self._fHandle.close()
                self._fHandle = None
