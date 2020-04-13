from constants.Covid19Constants import Covid19Constants
from covid19io.Covid19InputDownloader import Covid19InputDownloader
from covid19io.ExcelWriter import ExcelWriter
from covid19io.FileReader import FileReader
from data.ObsCollection import ObsCollection
from covid19io.Covid19Args import Covid19Args
from transform.CmdLineToLocation import CmdLineToLocation
from transform.Covid19USTransformer import Covid19USTransformer
from transform.Covid19Utils import Covid19Utils


if __name__ == '__main__':
    args = Covid19Args()
    args.setup()
    args.parse()

    if args.download:
        downloadFilename = args.downloadFilename()
        inputfile = Covid19InputDownloader.downloadFile(Covid19Constants.DOWNLOAD_URL,
                                                        downloadFilename)
        rdr = FileReader(inputfile)
        print('\nDownloaded file saved as "{0}".\n'.format(inputfile))
    else:
        rdr = FileReader(args.inputfile)

    tx = Covid19USTransformer();
    rdr.read(tx)
    coll = ObsCollection()
    print("Read {0} lines from input file.".format(len(tx.getCollection())))
    for covid19Obj in tx.getCollection():
        Covid19Utils.addCSVToObsCollection(covid19Obj, coll)

    writer = ExcelWriter(args.templateOutput, openExisting=True, hasMacros=True)
    writer._rowNum = 2

    for locStr in args.locationList:
        loc = CmdLineToLocation.makeLocation(locStr)
        print('Adding values for location "{0}/{1}/{2}".'.format(loc.country, loc.state, loc.county))
        for obs in coll.getObservations(loc):
            # outputTup = (loc.country, loc.state, loc.county, '', obs.obsDate.value.strftime('%m/%d/%Y'), obs.value)
            outputTup = (loc.country, loc.state, loc.county, '', obs.obsDate.value,
                         obs.value, obs.log2Value, obs.lnValue)
            writer.writeLine(outputTup, header_=False)
    writer.save(args.outputfile)
