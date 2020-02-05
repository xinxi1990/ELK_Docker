# -*- coding: utf-8 -*-

import time
import json
import requests

from kafka import KafkaProducer,KafkaConsumer
from pykafka import KafkaClient

producer = KafkaProducer(bootstrap_servers=['192.168.1.232:9092'])
 #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]


# for i in range(3):
#      msg = "msg %d" % i
#      print(msg)
#      producer.send('test', msg)
# producer.close()

msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test_1",
        "host": "xxxx",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict)
producer.send('test_rhj', msg, partition=0)
producer.close()

# from pykafka import KafkaClient
# client = KafkaClient(hosts="192.168.1.232:9092")
# #查看主题

# --------------------------------------------------------------------------------
# 下面是消费者的简单代码：
from kafka import KafkaConsumer

consumer = KafkaConsumer('test_rhj', bootstrap_servers=['192.168.1.232:9092'])
print(consumer)
for msg in consumer:
    print("################")
    print(msg)
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)
