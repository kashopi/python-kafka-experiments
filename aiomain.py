import sys
from aiokafka import AIOKafkaConsumer
import asyncio
from aiohttp import web

loop = asyncio.get_event_loop()

async def kafka_consumer(app):
    consumer = AIOKafkaConsumer(
        'mypart',
        loop=app.loop, bootstrap_servers='localhost:9092',
        group_id=group, max_poll_records=1)
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


async def start_kafka_task(app):
    app['kafka_listener'] = app.loop.create_task(kafka_consumer(app))


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


args = sys.argv
port, group = args[1:]

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

app.on_startup.append(start_kafka_task)
web.run_app(app, port=int(port))

