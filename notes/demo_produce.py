"""Demo secure Kafka producer

Demonstrates how to write messages to a Kafka cluster secured with SASL/SCRAM.
"""

from confluent_kafka import Producer
from random import randint

output_topic = 'lsst_test'
message = "Test message - " + str(randint(0, 9999))

settings = {
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'sasl.username': 'admin',
    'sasl.password': 'g3j8srri6b9'
}

p = Producer(settings)

try:
    p.produce(output_topic, message)
finally:
    p.flush()


