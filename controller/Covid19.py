from controller.Covid19Args import Covid19Args
from controller.Covid19CtrollerUtils import Covid19ControllerUtils
from covid19io.ExcelWriter import ExcelWriter
from transform.CmdLineToLocation import CmdLineToLocation




if __name__ == '__main__':
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
        for obs in coll.getObservations(loc):
            # outputTup = (loc.country, loc.state, loc.county, '', obs.obsDate.value.strftime('%m/%d/%Y'), obs.value)
            outputTup = (loc.country, loc.state, loc.county, '', loc.locationAsStr(), obs.obsDate.value,
                         obs.value, obs.log2Value, obs.lnValue)
            writer.writeLine(outputTup, header_=False)
    writer.save(args.outputfile)
