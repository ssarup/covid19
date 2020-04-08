from covid19io.FileReader import FileReader
from data.ObsCollection import ObsCollection
from covid19io.Covid19Args import Covid19Args
from transform.CmdLineToLocation import CmdLineToLocation
from transform.Covid19CSVTransformer import Covid19CSVTransformer
from transform.Covid19Utils import Covid19Utils


if __name__ == '__main__':
    args = Covid19Args()
    args.setup()

    rdr = FileReader(args.inputfile)
    tx = Covid19CSVTransformer();
    rdr.read(tx)
    coll = ObsCollection()
    print("Read {0} lines from input file.".format(len(tx.getCollection())))
    for covid19Obj in tx.getCollection():
        Covid19Utils.addCSVToObsCollection(covid19Obj, coll)

    # print(str(coll))

    print('Read the following locations ->')
    for loc in coll.locations():
        print(str(loc))

    for locStr in args.locationList:
        loc = CmdLineToLocation.makeLocation(locStr)
        print('Values for location "{0}/{1}/{2}" are ->'.format(loc.country, loc.state, loc.county))
        for obs in coll.getObservations(loc):
            print('"{0}","{1}",{2},{3}'.format(loc.state,loc.county,obs._obsDate._value.strftime('%m/%d/%Y'), obs._value))
        print("\n")
