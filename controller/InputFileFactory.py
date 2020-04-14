from enum import Enum, unique

from constants.Covid19Constants import Covid19Constants
from transform.Covid19GlobalTransformer import Covid19GlobalTransformer
from transform.Covid19USTransformer import Covid19USTransformer


@unique
class InputFileFactory(Enum):
    CONFIRMED_US     = 1
    CONFIRMED_GLOBAL = 2

    def downloadFilePrefix(self):
        if self == InputFileFactory.CONFIRMED_US:
            return Covid19Constants.US_CONFIRMED_FILE_PREFIX
        elif self == InputFileFactory.CONFIRMED_GLOBAL:
            return Covid19Constants.GLOBAL_CONFIRMED_FILE_PREFIX
        else:
            return None

    def downloadURL(self):
        if self == InputFileFactory.CONFIRMED_US:
            return Covid19Constants.US_CONFIRMED_URL
        elif self == InputFileFactory.CONFIRMED_GLOBAL:
            return Covid19Constants.GLOBAL_CONFIRMED_URL
        else:
            return None

    def covid19Transformer(self):
        if self == InputFileFactory.CONFIRMED_US:
            return Covid19USTransformer()
        elif self == InputFileFactory.CONFIRMED_GLOBAL:
            return Covid19GlobalTransformer()
        else:
            return None
