class ProducerConfig:
    def get_config(self):
        return {
            'bootstrap.servers': 'localhost:9092',
            'acks': 'all',
            'compression.codec': 'gzip',
            'enable.idempotence': True,
            'delivery.timeout.ms': 3000,
            'max.in.flight.requests.per.connection': 4
        }
