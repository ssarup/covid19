from shutil import copyfile
from unittest import TestCase
from covid19io.ExcelWriter import ExcelWriter


class TestExcelWriter(TestCase):
    def test_filename(self):
        exFile = ExcelWriter('')
        self.assertEqual('', exFile.filename)
        exFile = ExcelWriter('/Users/developer/Downloads/test.xlsx')
        self.assertEqual('/Users/developer/Downloads/test.xlsx', exFile.filename)
        self.assertIsNotNone(exFile._workbook)
        self.assertIsNotNone(exFile._worksheet)
        self.assertEqual('Sheet', exFile._activeSheetName)
        self.assertEqual(1, exFile._rowNum)
        self.assertEqual(1, exFile._column)

    def test_activeSheetName(self):
        exFile = ExcelWriter('/Users/developer/Downloads/test.xlsx')
        self.assertEqual('Sheet', exFile.activeSheetName)

    def test_set_active_sheet(self):
        exFile = ExcelWriter('/Users/developer/Downloads/test.xlsx')

        def test1():
            exFile.setActiveSheet('abc')
            self.assertEqual('abc', exFile.activeSheetName)
            self.assertIsNotNone(exFile._workbook)
            self.assertIsNotNone(exFile._worksheet)
            self.assertIsNotNone(exFile._rowNum)
            self.assertEqual(1, exFile._rowNum)
            self.assertIsNotNone(exFile._column)
            self.assertEqual(1, exFile._column)

        def test2():
            exFile.setActiveSheet('def')
            self.assertEqual('def', exFile.activeSheetName)
            self.assertIsNotNone(exFile._workbook)
            self.assertIsNotNone(exFile._worksheet)
            self.assertIsNotNone(exFile._rowNum)
            self.assertEqual(1, exFile._rowNum)
            self.assertIsNotNone(exFile._column)

        test1()
        self.assertTrue('abc' in exFile._workbook.sheetnames)
        test2()
        self.assertTrue('abc' in exFile._workbook.sheetnames)
        self.assertTrue('def' in exFile._workbook.sheetnames)

    def setUp(self):
        self._verifyList = [
            ('abc', '01/02/2020', 10),
            ('bcd', '01/03/2020', 20),
            ('cde', '01/04/2020', 30),
            ('def', '01/05/2020', 40),
            ('efg', '01/06/2020', 50),
        ]
        self._verifyListNew = [
            ('abc', '01/02/2020', 10),
            ('bcd', '01/03/2020', 20),
            ('cde', '01/04/2020', 30),
            ('def', '01/05/2020', 40),
            ('efg', '01/06/2020', 50),
            ('xyz', '01/06/2050', 500),
        ]

    def test_write_line(self):
        exFile = ExcelWriter('/Users/developer/Downloads/test.xlsx')

        def test1():
            exFile.setActiveSheet('abc')
            header = True
            for item in self._verifyList:
                exFile.writeLine(item, header)
                if header:
                    header = False
                else:
                    header = True

            self.assertEqual(len(self._verifyList), exFile._worksheet.max_row)
            self.assertEqual(len(self._verifyList) + 1, exFile._rowNum)
            self.assertEqual(1, exFile._column)
            self.assertEqual(3, exFile._worksheet.max_column)
            for i in range(1, exFile._worksheet.max_row):
                for j in range(1, 3):
                    currCell = exFile._worksheet.cell(row=i, column=j)
                    self.assertEqual(self._verifyList[i-1][j-1], currCell.value)

        def test2():
            exFile.setActiveSheet('def')
            header = True
            for item in self._verifyList[:-1]:
                exFile.writeLine(item, header)
                if header:
                    header = False
                else:
                    header = True

            self.assertEqual(len(self._verifyList) - 1, exFile._worksheet.max_row)
            self.assertEqual(len(self._verifyList), exFile._rowNum)
            self.assertEqual(1, exFile._column)
            self.assertEqual(3, exFile._worksheet.max_column)
            for i in range(1, exFile._worksheet.max_row):
                for j in range(1, 3):
                    currCell = exFile._worksheet.cell(row=i, column=j)
                    self.assertEqual(self._verifyList[i-1][j-1], currCell.value)

        test1()
        self.assertTrue('abc' in exFile._workbook.sheetnames)
        test2()
        self.assertTrue('abc' in exFile._workbook.sheetnames)
        self.assertTrue('def' in exFile._workbook.sheetnames)

    def test_save(self):
        exFile = ExcelWriter('/Users/developer/Downloads/test.xlsx')

        def test1():
            exFile.setActiveSheet('abc')
            header = True
            for item in self._verifyList:
                exFile.writeLine(item, header)
                if header:
                    header = False
                else:
                    header = True

            self.assertEqual(len(self._verifyList), exFile._worksheet.max_row)
            self.assertEqual(len(self._verifyList) + 1, exFile._rowNum)
            self.assertEqual(1, exFile._column)
            self.assertEqual(3, exFile._worksheet.max_column)

        def test2():
            exFile.setActiveSheet('def')
            header = True
            for item in self._verifyList[:-1]:
                exFile.writeLine(item, header)
                if header:
                    header = False
                else:
                    header = True

            self.assertEqual(len(self._verifyList) - 1, exFile._worksheet.max_row)
            self.assertEqual(len(self._verifyList), exFile._rowNum)
            self.assertEqual(1, exFile._column)
            self.assertEqual(3, exFile._worksheet.max_column)

        test1()
        test2()
        self.assertTrue('abc' in exFile._workbook.sheetnames)
        self.assertTrue('def' in exFile._workbook.sheetnames)
        exFile.save()

    def test_openExisting(self):
        copyfile('/Users/developer/Downloads/test.xlsx',
                 '/Users/developer/Downloads/test2.xlsx')
        exFile = ExcelWriter('/Users/developer/Downloads/test2.xlsx', openExisting=True)

        def test1():
            self.assertEqual('/Users/developer/Downloads/test2.xlsx', exFile.filename)
            self.assertIsNotNone(exFile._workbook)
            self.assertIsNotNone(exFile._worksheet)
            self.assertEqual('Sheet', exFile._activeSheetName)
            self.assertEqual(1, exFile._rowNum)
            self.assertEqual(1, exFile._column)

        def test2():
            # Remove existing sheet 'abc' before proceeding.
            self.assertTrue('abc' in exFile._workbook.sheetnames)
            exFile._workbook.remove(exFile._workbook['abc'])
            self.assertFalse('abc' in exFile._workbook.sheetnames)
            exFile.setActiveSheet('abc')
            header = True
            for item in self._verifyListNew:
                exFile.writeLine(item, header)
                if header:
                    header = False
                else:
                    header = True

            self.assertEqual(len(self._verifyListNew), exFile._worksheet.max_row)
            self.assertEqual(len(self._verifyListNew) + 1, exFile._rowNum)
            self.assertEqual(1, exFile._column)
            self.assertEqual(3, exFile._worksheet.max_column)

        def test3():
            # Remove existing sheet 'def' before proceeding.
            self.assertTrue('def' in exFile._workbook.sheetnames)
            exFile._workbook.remove(exFile._workbook['def'])
            self.assertFalse('def' in exFile._workbook.sheetnames)
            exFile.setActiveSheet('def')
            header = True
            for item in self._verifyListNew[:-1]:
                exFile.writeLine(item, header)
                if header:
                    header = False
                else:
                    header = True

            self.assertEqual(len(self._verifyListNew) - 1, exFile._worksheet.max_row)
            self.assertEqual(len(self._verifyListNew), exFile._rowNum)
            self.assertEqual(1, exFile._column)
            self.assertEqual(3, exFile._worksheet.max_column)

        test1()
        test2()
        test3()
        self.assertTrue('Sheet' in exFile._workbook.sheetnames)
        self.assertTrue('abc' in exFile._workbook.sheetnames)
        self.assertTrue('def' in exFile._workbook.sheetnames)
        exFile.save()
