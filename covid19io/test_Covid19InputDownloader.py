from unittest import TestCase
from datetime import datetime
import os
from constants.Covid19Constants import Covid19Constants
from covid19io.Covid19InputDownloader import Covid19InputDownloader


class TestCovid19InputDownloader(TestCase):
    def test_download_file(self):
        today = datetime.today()
        filename = '{0}/{1}_{2}.csv'.format(Covid19Constants.DOWNLOAD_FOLDER,
                                            Covid19Constants.CONFIRMED_FILE_PREFIX,
                                            today.strftime('%Y%m%d'))
        # fileWithPath = '{0}/{1}'.format(Covid19Constants.DOWNLOAD_FOLDER, filename)
        try:
            os.remove(filename)
        except:
            pass
        website = Covid19Constants.DOWNLOAD_URL

        outputFile = Covid19InputDownloader.downloadFile(website, filename)
        self.assertTrue(os.path.exists(filename))
        self.assertTrue(filename, outputFile)
