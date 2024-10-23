class Rabbit:
    def __init__(self, rabbit_url):
        self.rabbit_url = rabbit_url
        self._connection = None
        self._channel = None

    async def _connect(self):
        pass

    async def publish(self):
        pass

    async def consume(self):
        pass

    def _queue_declare(self):
        pass
