import os


class Covid19InputDownloader(object):
    _DOWNLOAD_FOLDER = '/Users/developer/Downloads/covid19'

    @staticmethod
    def downloadFile(website_, outputFile_):
        cmd = 'curl {0} -o {1}'.format(website_, outputFile_)
        os.system(cmd)
        return outputFile_
