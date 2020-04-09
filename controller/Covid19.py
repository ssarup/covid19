from covid19io.ExcelWriter import ExcelWriter
from covid19io.FileReader import FileReader
from data.ObsCollection import ObsCollection
from covid19io.Covid19Args import Covid19Args
from transform.CmdLineToLocation import CmdLineToLocation
from transform.Covid19CSVTransformer import Covid19CSVTransformer
from transform.Covid19Utils import Covid19Utils


if __name__ == '__main__':
    args = Covid19Args()
    args.setup()
    args.parse()

    rdr = FileReader(args.inputfile)
    tx = Covid19CSVTransformer();
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
            outputTup = (loc.country, loc.state, loc.county, '', obs.obsDate.value, obs.value)
            writer.writeLine(outputTup, header_=False)
    writer.save(args.outputfile)
