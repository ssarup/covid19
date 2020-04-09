from unittest import TestCase

from covid19io.OutputWriter import OutputWriter


class TestOutputWriter(TestCase):
    class MyWriter(OutputWriter):
        def __init__(self):
            self._strList = []

        def writeLine(self, tup_, header_):
            assert isinstance(header_, bool)
            tup = (str(tup_), header_)
            self._strList.append(tup)

    def setUp(self):
        self._verifyList = [
            ("('abc',)", True),
            ("('cde',)", True),
            ("('def', 'ghi')", False),
            ("('jkl',)", False)
        ]

    def test_write_line(self):
        wr = TestOutputWriter.MyWriter()
        for item in self._verifyList:
            wr.writeLine(item[0], item[1])
        i = 0
        for item1 in wr._strList:
            self.assertEqual(str(item1[0]), self._verifyList[i][0])
            self.assertEqual(item1[1], self._verifyList[i][1])
            # print(self._verifyList[i])
            # print(str(item1))
            # print(str(item1[0]) == self._verifyList[i][0])
            # print(item1[1] == self._verifyList[i][1])
            i = i + 1



