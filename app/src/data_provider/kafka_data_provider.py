import json
import logging
import uuid

from confluent_kafka import Producer

from app.src.config.producer_config import ProducerConfig
from app.src.interfaces.ievent_provider import IEventProvider


class KafkaDataProvider(IEventProvider):
    def __init__(self, config: ProducerConfig):
        self.__producer = Producer(config.get_config())
        self.__topic = 'my_stored_pokemon'

    def call_back(self, err, msg):
        if err is not None:
            self.__response = "Failed to deliver message: {0}: {1}".format(msg.value(), err.str())
        else:
            self.__response = json.loads(msg.value())

    def send(self, message: str):
        try:
            self.__producer.produce(self.__topic, key=str(uuid.uuid4()), value=message, callback=self.call_back)
            self.__producer.poll(0.5)
        except Exception as err:
            print(err)
        finally:
            self.__producer.flush()
        return self.__response
