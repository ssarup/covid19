from unittest import TestCase
from datetime import datetime
from controller.Covid19Args import Covid19Args
from constants.Covid19Constants import Covid19Constants
from controller.InputFileFactory import InputFileFactory


class TestCovid19Args(TestCase):
    def test__get_location_args(self):
        def test1():
            self.assertEqual([], Covid19Args._getLocationArgs(''))

        def test2():
            self.assertEqual([], Covid19Args._getLocationArgs('abc'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc.def'))
            self.assertEqual([], Covid19Args._getLocationArgs(' abc   '))
            self.assertEqual([], Covid19Args._getLocationArgs('/abc'))
            self.assertEqual([], Covid19Args._getLocationArgs('   /abc'))
            self.assertEqual([], Covid19Args._getLocationArgs(' / abc'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc/'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc  /'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc  / '))
            self.assertEqual([], Covid19Args._getLocationArgs('abc   /'))
            self.assertEqual([], Covid19Args._getLocationArgs('//'))
            self.assertEqual([], Covid19Args._getLocationArgs('///'))
            self.assertEqual(['a//'], Covid19Args._getLocationArgs('a//'))
            self.assertEqual(['a///'], Covid19Args._getLocationArgs('a///'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc/def'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc / def'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc /def'))
            self.assertEqual([], Covid19Args._getLocationArgs('abc xyz/def'))
            self.assertEqual(['abc/def/'], Covid19Args._getLocationArgs('abc/def/'))
            self.assertEqual(['abc / def/'], Covid19Args._getLocationArgs('abc / def/'))
            self.assertEqual(['abc / def /'], Covid19Args._getLocationArgs('abc / def /'))
            self.assertEqual(['abc /def/ghi'], Covid19Args._getLocationArgs('abc /def/ghi'))
            self.assertEqual(['abc /def/'], Covid19Args._getLocationArgs('abc /def/'))
            self.assertEqual(['abc xyz/def / mno '], Covid19Args._getLocationArgs('abc xyz/def / mno '))
            self.assertEqual(['India//'], Covid19Args._getLocationArgs('India//'))
            self.assertEqual(['India/ / '], Covid19Args._getLocationArgs('India/ / '))
            self.assertEqual(['India  //'], Covid19Args._getLocationArgs('India  //'))

        def test3():
            self.assertEqual([], Covid19Args._getLocationArgs('abc, def'))
            self.assertEqual(['abc/xyz/'], Covid19Args._getLocationArgs('abc/xyz/, def'))
            self.assertEqual(['abc/xyz/mno', 'def/ghi/jkl'],
                             Covid19Args._getLocationArgs('abc/xyz/mno, def/ghi/jkl'))
            self.assertEqual(['abc/xyz/mno', 'def jkl/ghi/jkl'],
                             Covid19Args._getLocationArgs('abc/xyz/mno, "def jkl"/ghi/jkl'))
            self.assertEqual(['abc/xyz/mno', 'def jkl/ghi stu/xyz', 'mno /pqr/'],
                             Covid19Args._getLocationArgs('abc/xyz/mno, "def jkl"/ghi stu/xyz, xyz, mno /pqr/'))

        test1()
        test2()
        test3()

    def test_downloadFilename(self):
        timeSuffix = 2014
        today = datetime.today().strftime('%Y%m%d')
        downloadFilenamesWithPath = Covid19Args.downloadFilenamesWithPath(timeSuffix)
        self.assertEqual(len(InputFileFactory), len(downloadFilenamesWithPath.keys()))
        for fileType in InputFileFactory:
            checkFilename = '{0}/{1}_{2}{3}.csv'.format(Covid19Constants.DOWNLOAD_FOLDER,
                                                        fileType.downloadFilePrefix(),
                                                        today, timeSuffix)
            self.assertEqual(checkFilename, downloadFilenamesWithPath[fileType])

    def test_setup(self):
        args = Covid19Args()
        self.assertIsNone(args._parser)
        self.assertIsNone(args._inputfile)
        self.assertIsNone(args._locationList)
        self.assertFalse(args.download)
        self.assertIsNone(args._templateOutputFile)
        self.assertIsNone(args._outputfile)
        args.setup()
        self.assertIsNotNone(args._parser)
        self.assertIsNone(args._inputfile)
        self.assertFalse(args.download)
        self.assertIsNone(args._locationList)
        self.assertIsNone(args._templateOutputFile)
        self.assertIsNone(args._outputfile)

    def test_parse(self):
        testList = ['--input', 'aaa',
                    '--location', 'bbb/ccc/ddd, eee/fff/ggg',
                    '--templateOutput', 'hhh',
                    '--download',
                    '--output', 'jjj']
        args = Covid19Args()

        def test_inputFile():
            self.assertIsNotNone(args.inputfile)
            self.assertEqual('aaa', args.inputfile)

        def test_globalInputfile():
            self.assertIsNotNone(args.inputfile)
            self.assertEqual('kkk', args.globalInputfile)

        def test_download():
            self.assertIsNotNone(args.download)
            # print(args.download)
            self.assertTrue(args.download)

        def test_locationList():
            self.assertIsNotNone(args.locationList)
            self.assertEqual(['bbb/ccc/ddd', 'eee/fff/ggg'], args.locationList)

        def test_templateOutputFile():
            self.assertIsNotNone(args.templateOutput)
            self.assertEqual('hhh', args.templateOutput)

        def test_outputFile():
            self.assertIsNotNone(args.outputfile)
            self.assertEqual('jjj', args.outputfile)

        args.setup()
        self.assertIsNotNone(args._parser)
        self.assertIsNone(args._inputfile)
        self.assertIsNone(args.globalInputfile)
        self.assertFalse(args.download)
        self.assertIsNone(args._locationList)
        self.assertIsNone(args._templateOutputFile)
        self.assertIsNone(args._outputfile)
        args.parse(testList)
        test_inputFile()
        test_locationList()
        test_templateOutputFile()
        test_outputFile()
        test_download()

        testList.append('--globalInput')
        testList.append('kkk')
        args.parse(testList)
        test_inputFile()
        test_locationList()
        test_templateOutputFile()
        test_outputFile()
        test_download()
        test_globalInputfile()
