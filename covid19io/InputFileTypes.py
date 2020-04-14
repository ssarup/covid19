from enum import Enum, unique

from constants.Covid19Constants import Covid19Constants


@unique
class InputFileTypes(Enum):
    CONFIRMED_US     = 1
    CONFIRMED_GLOBAL = 2

    def downloadFilePrefix(self):
        if self == InputFileTypes.CONFIRMED_US:
            return Covid19Constants.US_CONFIRMED_FILE_PREFIX
        elif self == InputFileTypes.CONFIRMED_GLOBAL:
            return Covid19Constants.GLOBAL_CONFIRMED_FILE_PREFIX
        else:
            return None
