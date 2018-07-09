import sys
from aiokafka import AIOKafkaProducer
import asyncio

loop = asyncio.get_event_loop()

async def send_one(filename):
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        with open(filename, "rb") as f:
            content = f.read()
        await producer.send_and_wait("jsontest", content)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

params = sys.argv
filename = params[1]

loop.run_until_complete(send_one(filename))