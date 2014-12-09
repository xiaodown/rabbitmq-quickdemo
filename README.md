rabbitmq-quickdemo
==================

## Quick tool for playing with rabbitmq

This is just two quick python scripts for dumping text on a queue, and pulling it in real time.  Useful for testing RabbitMQ.

### send.py

Send a message to rabbitmq on localhost.

If you have python in your path, invoke with `./send.py "message"`  

This will dump a message of `message` on a queue called `hello`.  To change the queue, edit send.py and change the line:
```python
channel.queue_declare(queue='hello')
```
to something else.

### receive.py

Receive a message from rabbitmq on localhost.

Again, to change the queue it consumes, edit `channel.queue_declare(queue='hello')` to something else.

Invoke with `./receive.py` if you have python in your path, and `Ctl-C` to stop consuming the queue.

### Requirements / setup

You'll need to have a few things installed.  These instructions, where specific, are for Centos (~6) but are easily adaptable to Ubuntu by replacing `yum` with `apt-get` where needed.

Also note, this is just to demo this script; for example, turning iptables off just means you can get into the management web page without futzing, but is obviously a bad idea.  

```bash
 * yum install -y git vim python-pika rabbitmq-server
 * service iptables stop
 * service rabbitmq-server start
 * curl localhost:5672 (verify that it's AMQP)
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins list
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management
 * service rabbitmq-server restart
 * http://rabbitdemo.foo.bar.baz:15672/ guest/guest (log into the web console\*)
 * git clone https://github.com/xiaodown/rabbitmq-quickdemo.git
 * for i in pants boots socks shirts undaroos ; do rabbitmq-quickdemo/send.py $i ;done
 * rabbitmq-quickdemo/receive.py 
```

