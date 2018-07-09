import sys
import random
from aiokafka import AIOKafkaProducer
import asyncio

loop = asyncio.get_event_loop()

async def send_one():
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        calls = []
        for i in range(0, count):
            partition = random.randint(0,2)
            print(f"Using partition {partition}")
            calls.append(
                producer.send_and_wait("mypart", str.encode(f"Super message {i}"), partition=partition))
        await asyncio.gather(*calls)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

args = sys.argv
count = int(args[1])
loop.run_until_complete(send_one())