import sys
from aiokafka import AIOKafkaConsumer
import asyncio
from aiohttp import web

loop = asyncio.get_event_loop()


async def consume():
    consumer = AIOKafkaConsumer(
        'mypart',
        loop=loop, bootstrap_servers='localhost:9092',
        group_id=group, max_poll_records=1)
    print(f'Connected to Kafak Group {group}')
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

args = sys.argv
group = args[1]

loop.run_until_complete(consume())
