from data.Location import Location


class CmdLineToLocation(object):
    """
    Convert from command line strings to Location objects.
    Command line strings can be in the following format -
        Country/State/County
    """

    @staticmethod
    def makeLocation(locStr_):
        if locStr_.count('/') >= 2:
            locPartList = locStr_.split('/')
            return Location(str(locPartList[0]).strip(),
                            str(locPartList[1]).strip(),
                            str(locPartList[2]).strip())
