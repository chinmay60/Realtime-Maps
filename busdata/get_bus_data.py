from google.transit import gtfs_realtime_pb2
import os
import requests

#Get live bus data from GoMetro Cincinnati
class GetbusData:
    def main():
        feed = gtfs_realtime_pb2.FeedMessage()
        url = ('http://developer.go-metro.com/TMGTFSRealTimeWebService/vehicle/VehiclePositions.pb')
        get_feed(feed, url)


    def get_feed(feed, url):
        response = requests.get(url, allow_redirects=True)
        feed.ParseFromString(response.content)
        with open('output.txt', mode='w') as f:
            for entity in feed.entity:
                f.write(str(entity))


    if __name__ == "__main__":
        main()