import logging
import math
import time

import pika
from pika.adapters.blocking_connection import BlockingConnection, BlockingChannel

logging.basicConfig(level=logging.INFO)


class Rabbit:
    def __init__(self, rabbit_url):
        self.rabbit_url = rabbit_url
        self._connection: BlockingConnection = None
        self._channel: BlockingChannel = None

    async def _connect(self):
        counts = 0

        while True:
            try:
                connection = pika.BlockingConnection(pika.URLParameters(self.rabbit_url))
                channel = connection.channel()
                logging.info("Connected to the rabbitMQ")
                break
            except Exception as e:
                logging.warning("rabbitmq not yet ready...")
                counts += 1

                if counts > 5:
                    logging.error(f"Failed to connect to RabbitMQ: {e}")
                    return

                back_off = math.pow(counts, 2)
                logging.info(f"Backing off for {back_off} seconds")

                time.sleep(back_off)

        self._connection = connection
        self._channel = channel

    async def publish(self, routing_key, data):
        pass

    async def consume(self, routing_key):
        pass

    def _queue_declare(self):
        pass
