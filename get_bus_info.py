
import json
import sys
import urllib2
import csv

if __name__=='__main__':
    MTA_KEY = sys.argv[1]
    BUS_LINE = sys.argv[2]

    # make new csv file
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

        # Load json file from MTA          
        url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (MTA_KEY, BUS_LINE)
        request = urllib2.urlopen(url)
        response = json.loads(request.read())

        # write the bus location and stop information to csv file
        for vehicle in response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
            Lat = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Lon = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            Stopname = vehicle['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
            Stopstatus = vehicle['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            writer.writerow([Lat, Lon, Stopname, Stopstatus])


    

