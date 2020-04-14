from unittest import TestCase
from constants.Covid19Constants import Covid19Constants
from covid19io.InputFileTypes import InputFileTypes


class TestInputFileTypes(TestCase):
    def test_download_file_prefix(self):
        def testUS():
            ty = InputFileTypes.CONFIRMED_US
            self.assertEqual(InputFileTypes, type(ty))
            self.assertEqual(InputFileTypes.CONFIRMED_US, ty)
            self.assertEqual(InputFileTypes.CONFIRMED_US.value, ty.value)
            self.assertEqual(Covid19Constants.US_CONFIRMED_FILE_PREFIX, ty.downloadFilePrefix())
        
        def testGlobal():
            ty = InputFileTypes.CONFIRMED_GLOBAL
            self.assertEqual(InputFileTypes, type(ty))
            self.assertEqual(InputFileTypes.CONFIRMED_GLOBAL, ty)
            self.assertEqual(InputFileTypes.CONFIRMED_GLOBAL.value, ty.value)
            self.assertEqual(Covid19Constants.GLOBAL_CONFIRMED_FILE_PREFIX, ty.downloadFilePrefix())

        testUS()
        testGlobal()

