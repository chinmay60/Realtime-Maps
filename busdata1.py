
from pykafka import KafkaClient

client = KafkaClient(hosts="localhost:9092")

topic = client.topics['TestBusData']

producer = topic.get_sync_producer()

producer.produce('test message'.encode('ascii'))
