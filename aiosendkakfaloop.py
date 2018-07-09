import sys
import random
from aiokafka import AIOKafkaProducer
import asyncio
from time import sleep

loop = asyncio.get_event_loop()

async def send_one():
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        count = 0
        while True:            
            await producer.send_and_wait("mypart", str.encode(f"Super message {count}"))
            count = count + 1
            sleep(wait)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

args = sys.argv
wait = float(args[1])
loop.run_until_complete(send_one())