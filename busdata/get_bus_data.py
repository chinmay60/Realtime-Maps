from google.transit import gtfs_realtime_pb2
import requests

#Get live bus data from GoMetro Cincinnati
class GetbusData:
    def __init__(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        url = ('http://developer.go-metro.com/TMGTFSRealTimeWebService/vehicle/VehiclePositions.pb')
        self.get_feed(feed, url)

#get the bus feed 
    def get_feed(self, feed, url):
        response = requests.get(url, allow_redirects=True)
        feed.ParseFromString(response.content)
        with open('output.txt', mode='w') as f:
            for entity in feed.entity:
                f.write(str(entity))


    