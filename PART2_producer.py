import pika
import json
from datetime import datetime

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


channel.exchange_declare(exchange='HW8', exchange_type='fanout', durable=True)
# channel.queue_declare(queue='home_work_8', durable=True)
# channel.queue_bind(exchange='HW-8', queue='home_work_8')


# def create_tasks(nums: int):
#     for i in range(nums):
#         message = {
#             'id': i,
#             'payload':f"{datetime.now().isoformat()}",
#         }
#         channel.basic_publish(exchange='HW-8', routing_key='home_work_8', body=json.dumps(message).encode())
#     connection.close()

def create_event(nums: int):
    message = {
            'event': 'Test event',
            'message': 'My message',
            'detail': f"{datetime.now().isoformat()}",
    }
    channel.basic_publish(exchange='HW8', routing_key='', body=json.dumps(message).encode())
    connection.close()



if __name__ == '__main__':
    # create_tasks(100)
    create_event(100)