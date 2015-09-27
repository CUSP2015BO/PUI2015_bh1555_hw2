
import json
import sys
import urllib2

if __name__=='__main__':
    MTA_KEY = sys.argv[1]
    BUS_LINE = sys.argv[2]
              
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (MTA_KEY, BUS_LINE)
    request = urllib2.urlopen(url)
    response = json.loads(request.read())
       
    # Count the number of active buses
    NUM_BUS = len(response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

    # print bus line and the number of active buses
    print "Bus Line : %s" % (BUS_LINE)
    print "Number of Active Buses : %s"  % (NUM_BUS)
    
    # print location of each active bus by using for loop 
    i=0
    for vehicle in response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']:
        Lat = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        Lon = vehicle['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        i+=1
        print " * Bus %s is at latitude %s and longitude %s" % (i, Lat, Lon)
