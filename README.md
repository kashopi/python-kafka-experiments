# A small python asycio kafak examples

A very tiny python kafka experiment. To use and play with it you can setup the perfect confluent
kafka server on your system.


## Prepare you setup

Download from [Confluent](https://www.confluent.io/download/)

Extract the tar file go to the confluent folder and start the server with:

```
./bin/confluent start
```

To use the examples you have to create a queue.

```
./bin/kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 5 --topic mypart
```

## Let's start


Now you can start one consumer with:

```
python aiomain.py mygroup
```

mygroup is the name of the group that you want to join.

Open another shell and start to send some messages

```
python aiosendloop.py 0.01
```

These command is sending a message every 0.01 seconds.

You should now see the incominging messages in the consumer shell.

Now you can open another shell with the aiomain.py mygroup script. You will see that now every message is received only one time
by the one of the two running consumer scripts. If you want to split the message too two aiomain consumer create unique names 
for the consumer .

e.g.

```
python aiomain.py mygroup1
```

```
python aiomain.py mygroup2
```






