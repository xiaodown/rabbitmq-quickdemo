#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

total = len(sys.argv)
if total < 2:
	print "Must have one argument for the message body"
	sys.exit(1)
body = str(sys.argv[1])

channel.basic_publish(exchange='', routing_key='hello', body=body)
print " [x] Sent " + body
connection.close()
