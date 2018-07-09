import json
from datetime import datetime
from aiokafka import AIOKafkaProducer
import asyncio

loop = asyncio.get_event_loop()

async def send_one():
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        content = {}
        for i in range(90000):
            content[str(1)] = "abcdeftejla" * i
        dump = json.dumps(content)
        print(f"Message size {len(dump)/1024/1024} MB {len(dump)} bytes")
        start = datetime.now()
        await producer.send_and_wait("mypart", str.encode(dump))
        print(f"Time needed to send: {datetime.now()-start}")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

loop.run_until_complete(send_one())