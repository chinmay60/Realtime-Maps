
from pykafka import KafkaClient
import json
from datetime import datetime
import uuid

#Read coordinates from geoJason

input_file = open('./data/bus3.json')
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']

#generate UUID


def generate_uuid():
    return uuid.uuid4()


#kafka producer
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['geodata_final']
producer = topic.get_sync_producer()


#construct message

data = {}
data['busline'] = '00003'


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
      

        #if the bus reaches the last coordinate, start from the beginning
        if i == len(coordinates) - 1:
            i = 0
        i += 1


generate_checkpoint(coordinates)
