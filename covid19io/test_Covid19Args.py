from unittest import TestCase
from covid19io.Covid19Args import Covid19Args


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
            self.assertEqual(['abc/def'], Covid19Args._getLocationArgs('abc/def'))
            self.assertEqual(['abc / def'], Covid19Args._getLocationArgs('abc / def'))
            self.assertEqual(['abc /def'], Covid19Args._getLocationArgs('abc /def'))
            self.assertEqual(['abc xyz/def'], Covid19Args._getLocationArgs('abc xyz/def'))

        def test3():
            self.assertEqual([], Covid19Args._getLocationArgs('abc, def'))
            self.assertEqual(['abc/xyz'], Covid19Args._getLocationArgs('abc/xyz, def'))
            self.assertEqual(['abc/xyz', 'def/ghi'], Covid19Args._getLocationArgs('abc/xyz, def/ghi'))
            self.assertEqual(['abc/xyz', 'def jkl/ghi'], Covid19Args._getLocationArgs('abc/xyz, "def jkl"/ghi'))
            self.assertEqual(['abc/xyz', 'def jkl/ghi', 'mno /pqr'],
                             Covid19Args._getLocationArgs('abc/xyz, "def jkl"/ghi, xyz, mno /pqr'))

        test1()
        test2()
        test3()

    def test_setup(self):
        args = Covid19Args()
        self.assertIsNone(args._parser)
        self.assertIsNone(args._inputfile)
        self.assertIsNone(args._locationList)
        self.assertIsNone(args._templateOutputFile)
        self.assertIsNone(args._outputfile)
        args.setup()
        self.assertIsNotNone(args._parser)
        self.assertIsNone(args._inputfile)
        self.assertIsNone(args._locationList)
        self.assertIsNone(args._templateOutputFile)
        self.assertIsNone(args._outputfile)

    def test_parse(self):
        testList = [ '--input', 'aaa',
                     '--location', 'bbb/ccc/ddd, eee/fff/ggg',
                     '--templateOutput', 'hhh',
                     '--output', 'jjj']
        args = Covid19Args()

        def test_inputFile():
            self.assertIsNotNone(args.inputfile)
            self.assertEqual('aaa', args.inputfile)

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
        self.assertIsNone(args._locationList)
        self.assertIsNone(args._templateOutputFile)
        self.assertIsNone(args._outputfile)
        args.parse(testList)
        test_inputFile()
        test_locationList()
        test_templateOutputFile()
        test_outputFile()
