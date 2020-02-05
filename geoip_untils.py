
import json
import time
import requests
import geoip2.database
from logzero import logger
from kafka import KafkaProducer, KafkaConsumer
from pykafka import KafkaClient


file_path = "/Users/xinxi/Documents/sndd/crawlerfeedback/static/downloaded_data.log"

reader = geoip2.database.Reader('./static/GeoLite2-City.mmdb')
producer = KafkaProducer(bootstrap_servers=['192.168.1.232:9092'])
# response = reader.city('118.254.223.207')
# print(response.country.iso_code)
# print(response.country.names['zh-CN'])
# print(response.city.name)
# print(response.subdivisions.most_specific.name)
# print(response.postal.code)
# print(response.location.latitude)
# print(response.location.longitude)


with open(file_path) as f:
     info = f.readlines()

for i in  info:
    ip = json.loads(i)['client_ip']
    msg_dict = {
        "ip": ip
    }
    msg = json.dumps(msg_dict)
    logger.info("####################### \n{0} #######################".format(msg))
    producer.send('nginx-accesslog', msg_dict, partition=0)


producer.close()
reader.close()



