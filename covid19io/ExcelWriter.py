import openpyxl
from covid19io.OutputWriter import OutputWriter


class ExcelWriter(OutputWriter):
    def __init__(self, filename_):
        self._filename = filename_
        self._workbook = openpyxl.Workbook()
        self._activeSheetName = None
        self._worksheet = None
        self._rowNum = None
        self._column = None

    # def writeColumns(self, tuple_, worksheet_, lineNum_, colNum_):
    #     assert isinstance(worksheet_, worksheet)
    #     i = 0
    #     for item in tuple_:
    #         currCell = worksheet_.cell(row=lineNum_, column=colNum_+i)
    #         currCell.value = str(item)
    #         i = i + 1
    #
    # def writeLine(self, list_, worksheet_, lineNum_):
    #     assert isinstance(worksheet_, worksheet)
    #     i = 0
    #     for item in list_:
    #         self.writeColumns(item, worksheet_, i, 1)
    #         i = i + 1

    @property
    def filename(self):
        return self._filename

    @property
    def activeSheetName(self):
        return self._activeSheetName

    def setActiveSheet(self, sheetName_):
        self._worksheet = self._workbook.create_sheet(sheetName_)
        self._activeSheetName = sheetName_
        self._rowNum = 1
        self._column = 1

    def writeLine(self, tup_, header_):
        assert isinstance(tup_, tuple)
        assert isinstance(header_, bool)
        for item in tup_:
            currCell = self._worksheet.cell(row=self._rowNum, column=self._column)
            currCell.value = str(item)
            self._column = self._column + 1
        self._rowNum = self._rowNum + 1
        self._column = 1

    def save(self):
        self._workbook.save(filename=self._filename)

