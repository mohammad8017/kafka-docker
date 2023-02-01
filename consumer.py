from kafka import KafkaConsumer
from json import loads
from time import sleep

# topics=['topic_test', 'topic_test2']
topic = 'topic_test'
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='tt',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
# consumer.subscribe(topics=topics)

for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(f'consumer ---- topic : {topic} ---- recieved data : {event_data}')
    print('===================================')
    sleep(2)