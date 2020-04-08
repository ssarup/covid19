from unittest import TestCase
from data.Location import Location
from transform.CmdLineToLocation import CmdLineToLocation


class TestCmdLineToLocation(TestCase):
    def test_make_location(self):
        def test1():
            self.assertIsNone(CmdLineToLocation.makeLocation(''))
            self.assertIsNone(CmdLineToLocation.makeLocation('abc'))
            self.assertIsNone(CmdLineToLocation.makeLocation('/'))
            self.assertIsNone(CmdLineToLocation.makeLocation('abc/def'))
            loc = Location('abc', 'def', 'ghi')
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def/ghi'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def/ghi/jkl'))

        def test2():
            loc = Location('abc', 'def', 'ghi')
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation(' abc/def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc /def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/ def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def /ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def/ ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def/ghi /jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc/def/ghi/ jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc / def / ghi / jhk'))


        def test3():
            loc = Location('abc xyz', 'def', 'ghi')
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc xyz/def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation(' abc xyz/def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc xyz /def/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation(' abc xyz /def/ghi/jhk'))
            loc = Location('abc xyz', 'def mno', 'ghi')
            # print(str(loc), loc.state, Location('abc xyz', 'def mno', 'ghi').state)
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc xyz/def mno/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc xyz/ def mno/ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc xyz/def mno /ghi/jhk'))
            self.assertEqual(loc, CmdLineToLocation.makeLocation('abc xyz/ def mno /ghi/jhk'))

        test1()
        test2()
        test3()
