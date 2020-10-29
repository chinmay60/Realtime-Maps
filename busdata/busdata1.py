
from pykafka import KafkaClient
from get_bus_data import *
import json
from datetime import datetime
import uuid
import time



#Read coordinates from geoJason

input_file = open('./data/bus1.json')
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']

#generate UUID


def generate_uuid():
    return uuid.uuid4()


#kafka producer
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['final_geodata']
producer = topic.get_sync_producer()


#construct message

data = {}
data['busline'] = '00001'





def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):

        data['key'] = data['busline'] + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)
        print(message)
        producer.produce(message.encode('ascii'))
        time.sleep(1)
      

        #If the bus reaches the last coordinate, start from the beginning
        if i == len(coordinates) - 1:
            i = 0
        i += 1


generate_checkpoint(coordinates)
