import json
import time

import pika
import sys
import os


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    # channel.queue_declare(queue='home_work_8', durable=True)
    q = channel.queue_declare('', exclusive=True)
    name_q = q.method.queue
    channel.queue_bind(exchange='HW8', queue=name_q)

    def callback(ch, method, properties, body):
        message = json.loads(body.decode('utf-8'))
        print(f" [x] Received {message}")

    channel.basic_consume(queue=name_q, on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
