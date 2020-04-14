from unittest import TestCase
from controller.Covid19Args import Covid19Args


class TestCovid19ControllerUtils(TestCase):
    def test_setup_inputs_from_args(self):
        def testForDownload():
            args = Covid19Args()
            args.setup()
            argList = ['--input', 'aaa']

            def testNoDownloadArg():
                args.parse(argList)
                self.assertIsFalse(args.download)

            testNoDownloadArg()

        def testForUSInput():
            pass

        def testForGlobalInput():
            pass

        def testForAllInput():
            pass

        testForDownload()
        testForUSInput()
        testForGlobalInput()
        testForAllInput()

    def test_create_ObsCollection(self):
        pass
