from unittest import TestCase
from constants.Covid19Constants import Covid19Constants
from controller.InputFileFactory import InputFileFactory
from transform.Covid19GlobalTransformer import Covid19GlobalTransformer
from transform.Covid19USTransformer import Covid19USTransformer


class TestInputFileFactory(TestCase):
    def test_download_file_prefix(self):
        def testUS():
            ty = InputFileFactory.CONFIRMED_US
            self.assertEqual(InputFileFactory, type(ty))
            self.assertEqual(InputFileFactory.CONFIRMED_US, ty)
            self.assertEqual(InputFileFactory.CONFIRMED_US.value, ty.value)
            self.assertEqual(Covid19Constants.US_CONFIRMED_FILE_PREFIX, ty.downloadFilePrefix())
        
        def testGlobal():
            ty = InputFileFactory.CONFIRMED_GLOBAL
            self.assertEqual(InputFileFactory, type(ty))
            self.assertEqual(InputFileFactory.CONFIRMED_GLOBAL, ty)
            self.assertEqual(InputFileFactory.CONFIRMED_GLOBAL.value, ty.value)
            self.assertEqual(Covid19Constants.GLOBAL_CONFIRMED_FILE_PREFIX, ty.downloadFilePrefix())

        testUS()
        testGlobal()

    def test_download_URL(self):
        def testUS():
            ty = InputFileFactory.CONFIRMED_US
            self.assertEqual(InputFileFactory, type(ty))
            self.assertEqual(InputFileFactory.CONFIRMED_US, ty)
            self.assertEqual(InputFileFactory.CONFIRMED_US.value, ty.value)
            self.assertEqual(Covid19Constants.US_CONFIRMED_URL, ty.downloadURL())

        def testGlobal():
            ty = InputFileFactory.CONFIRMED_GLOBAL
            self.assertEqual(InputFileFactory, type(ty))
            self.assertEqual(InputFileFactory.CONFIRMED_GLOBAL, ty)
            self.assertEqual(InputFileFactory.CONFIRMED_GLOBAL.value, ty.value)
            self.assertEqual(Covid19Constants.GLOBAL_CONFIRMED_URL, ty.downloadURL())

        testUS()
        testGlobal()

    def test_covid19_Transformer(self):
        def testUS():
            ty = InputFileFactory.CONFIRMED_US
            self.assertEqual(InputFileFactory, type(ty))
            self.assertEqual(InputFileFactory.CONFIRMED_US, ty)
            self.assertEqual(InputFileFactory.CONFIRMED_US.value, ty.value)
            self.assertEqual(Covid19USTransformer, type(ty.covid19Transformer()))

        def testGlobal():
            ty = InputFileFactory.CONFIRMED_GLOBAL
            self.assertEqual(InputFileFactory, type(ty))
            self.assertEqual(InputFileFactory.CONFIRMED_GLOBAL, ty)
            self.assertEqual(InputFileFactory.CONFIRMED_GLOBAL.value, ty.value)
            self.assertEqual(Covid19GlobalTransformer, type(ty.covid19Transformer()))

        testUS()
        testGlobal()
