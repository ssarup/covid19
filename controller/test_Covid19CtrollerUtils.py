from unittest import TestCase
from controller.Covid19Args import Covid19Args
from controller.Covid19CtrollerUtils import Covid19ControllerUtils
from controller.InputFileFactory import InputFileFactory


class TestCovid19ControllerUtils(TestCase):
    def test_setup_inputs_from_args(self):
        def testForDownload():
            args = Covid19Args()
            args.setup()
            argList = ['--input', 'aaa',
                       '--download',
                       '--location', 'bbb/ccc/ddd, eee/fff/ggg',
                       '--templateOutput', 'hhh',
                       '--output', 'jjj']

            args.parse(argList)
            self.assertTrue(args.download)
            tupList = Covid19ControllerUtils.setupInputsFromArgs(args)
            filesFromArgs = Covid19Args.downloadFilenamesWithPath()
            self.assertEqual(len(filesFromArgs.keys()), len(tupList))
            for tup in tupList:
                fileType = tup[0]
                self.assertIn(fileType, filesFromArgs.keys())
                self.assertEqual(filesFromArgs[fileType], tup[1])
            fileTypeSet = set(filesFromArgs.keys())
            typeListFromTupeList = []
            for item in tupList:
                typeListFromTupeList.append(item[0])
            self.assertEqual(fileTypeSet, set(typeListFromTupeList))

        def testForUSInput():
            args = Covid19Args()
            args.setup()
            argList = ['--input', 'aaa',
                       '--location', 'bbb/ccc/ddd, eee/fff/ggg',
                       '--templateOutput', 'hhh',
                       '--output', 'jjj']

            args.parse(argList)
            self.assertFalse(args.download)
            tupList = Covid19ControllerUtils.setupInputsFromArgs(args)
            self.assertEqual(1, len(tupList))
            fileType = tupList[0][0]
            self.assertEqual(fileType, InputFileFactory.CONFIRMED_US)
            self.assertEqual('aaa', tupList[0][1])

        def testForGlobalInput():
            args = Covid19Args()
            args.setup()
            argList = ['--global', 'aaa',
                       '--location', 'bbb/ccc/ddd, eee/fff/ggg',
                       '--templateOutput', 'hhh',
                       '--output', 'jjj']

            args.parse(argList)
            self.assertFalse(args.download)
            tupList = Covid19ControllerUtils.setupInputsFromArgs(args)
            self.assertEqual(1, len(tupList))
            fileType = tupList[0][0]
            self.assertEqual(fileType, InputFileFactory.CONFIRMED_GLOBAL)
            self.assertEqual('aaa', tupList[0][1])

        def testForAllInput():
            args = Covid19Args()
            args.setup()
            argList = ['--input', 'aaa',
                       '--global', 'kkk',
                       '--location', 'bbb/ccc/ddd, eee/fff/ggg',
                       '--templateOutput', 'hhh',
                       '--output', 'jjj']

            args.parse(argList)
            self.assertFalse(args.download)
            tupList = Covid19ControllerUtils.setupInputsFromArgs(args)
            self.assertEqual(2, len(tupList))
            fileType = tupList[0][0]
            self.assertEqual(fileType, InputFileFactory.CONFIRMED_US)
            self.assertEqual('aaa', tupList[0][1])
            fileType = tupList[1][0]
            self.assertEqual(fileType, InputFileFactory.CONFIRMED_GLOBAL)
            self.assertEqual('kkk', tupList[1][1])

        # testForDownload()
        testForUSInput()
        testForGlobalInput()
        testForAllInput()

    def test_create_ObsCollection(self):
        pass
