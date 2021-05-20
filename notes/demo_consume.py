"""Demo public Kafka consumer 

Demonstrates how to read messages from the public Kafka cluster.
"""

from confluent_kafka import Consumer

input_topic = 'lsst_test'

settings = { 
    'bootstrap.servers': 'localhost:80',
    'group.id': 'demo',
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

c = Consumer(settings)
c.subscribe([input_topic])

n = 0
try:
    while n < 10:
        msg = c.poll(20)
        if msg is None:
            break
        elif not msg.error():
            print("Message: " + str(msg.value()))
            n += 1
        else:
            print(str(msg.error()))
            n += 1
finally:
    c.close()


