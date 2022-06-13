from confluent_kafka import Consumer, KafkaError


class ReadMessageFromKafka:
    def __init__(self, group_id, client_id, topic_list):
        self.__settings = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': group_id,
            'client.id': client_id,
            'enable.auto.commit': True,
            'session.timeout.ms': 6000,
            'default.topic.config': {'auto.offset.reset': 'smallest'}
        }
        self.__consumer = Consumer(self.__settings)
        self.__consumer.subscribe(topic_list)

    def read_message(self):
        try:
            while True:
                msg = self.__consumer.poll(0.1)
                if msg is None:
                    continue
                elif not msg.error():
                    print('Received message: {0}'.format(msg.value()))
                elif msg.error().code() == KafkaError._PARTITION_EOF:
                    print('End of partition reached {0}/{1}'
                          .format(msg.topic(), msg.partition()))
                else:
                    print('Error occured: {0}'.format(msg.error().str()))
        except Exception as exception:
            raise exception
        finally:
            self.__consumer.close()
