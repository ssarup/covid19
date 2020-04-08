from covid19io.FileReader import FileReader
from data.Location import Location
from data.ObsCollection import ObsCollection
from transform.Covid19CSVTransformer import Covid19CSVTransformer
from transform.Covid19Utils import Covid19Utils


if __name__ == '__main__':
    rdr = FileReader('/Users/developer/Downloads/time_series_covid19_confirmed_US-2.csv')
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

    print('Values for Middlesex county are ->')
    myLoc = Location('USA', 'New Jersey', 'Middlesex')
    for obs in coll.getObservations(myLoc):
        print('"{0}","{1}",{2},{3}'.format(myLoc.state,myLoc.county,obs._obsDate._value.strftime('%m/%d/%Y'), obs._value))
