from json import load
import os
from flask import Flask
from threading import Thread
from dotenv import load_dotenv
import pika
import time

sleepTime = 10
load_dotenv()
app = Flask(__name__)

if __name__ == '__main__':
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        cmd = body.decode()
        print(cmd)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()
