from controller.Covid19Args import Covid19Args
from controller.Covid19CtrollerUtils import Covid19ControllerUtils
from covid19io.ExcelWriter import ExcelWriter
from transform.CmdLineToLocation import CmdLineToLocation




if __name__ == '__main__':
    """
    Usage: 
        python3 controller/Covid19.py 
            --input "/Users/developer/Downloads/covid19/time_series_covid19_confirmed_US_202004141835.csv" 
            --global "/Users/developer/Downloads/covid19/time_series_covid19_confirmed_global_202004141835.csv" 
            --location "USA/New York/New York, USA/New York/Nassau, USA/New York/Westchester, USA/New York/Rockland, USA/New Jersey/Bergen, USA/New Jersey/Hudson, USA/New Jersey/Middlesex, USA/New Jersey/Mercer, USA/Connecticut/Fairfield, USA/Washington/King, USA/California/Santa Clara, USA/Illinois/Cook, United Kingdom//, India//" 
            --templateOutput "/Users/developer/Downloads/covid19Template7.xlsm" 
            --output "/Users/developer/Downloads/covid19/covid19.xlsm"
            
        python3 controller/Covid19.py 
            --download 
            --location "USA/New York/New York, USA/New York/Nassau, USA/New York/Westchester, USA/New York/Rockland, USA/New Jersey/Bergen, USA/New Jersey/Hudson, USA/New Jersey/Middlesex, USA/New Jersey/Mercer, USA/Connecticut/Fairfield, USA/Washington/King, USA/California/Santa Clara, USA/Illinois/Cook, United Kingdom//, India//" 
            --templateOutput "/Users/developer/Downloads/covid19Template7.xlsm" 
            --output "/Users/developer/Downloads/covid19/covid19.xlsm"
    """
    args = Covid19Args()
    args.setup()
    args.parse()

    inputList = Covid19ControllerUtils.setupInputsFromArgs(args)

    obsColl = Covid19ControllerUtils.createObsCollection(inputList)

    writer = ExcelWriter(args.templateOutput, openExisting=True, hasMacros=True)
    writer._rowNum = 2

    print('xx', str(args.locationList))
    for locStr in args.locationList:
        # print('xx', locStr)
        loc = CmdLineToLocation.makeLocation(locStr)
        print('Adding values for location "{0}".'.format(loc.locationAsStr()))
        for obs in obsColl.getObservations(loc):
            # outputTup = (loc.country, loc.state, loc.county, '', obs.obsDate.value.strftime('%m/%d/%Y'), obs.value)
            outputTup = (loc.country, loc.state, loc.county, '', loc.locationAsStr(), obs.obsDate.value,
                         obs.value, obs.log2Value, obs.lnValue)
            writer.writeLine(outputTup, header_=False)
    writer.save(args.outputfile)
