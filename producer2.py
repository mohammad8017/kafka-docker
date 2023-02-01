from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
for j in range(999):
    
    # data = {'counter': j}
    data = f'2.{j}th data'
    if j% 2 == 0:
        print(f"producer2 ---- Iteration : 2.{j} ---- topic : topic_test")
        print('===================================')
        producer.send('topic_test', value=data)
    else:
        print(f"producer2 ---- Iteration : 2.{j} ---- topic : topic_test2")
        print('===================================')
        producer.send('topic_test2', value=data)
    
    sleep(2)