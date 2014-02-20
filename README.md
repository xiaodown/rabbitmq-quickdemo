rabbitmq-quickdemo
==================

prior to demo:

 * yum install git vim 

Commands for to make demo:

 * yum install rabbitmq-server -y
 * service iptables stop
 * service rabbitmq-server start
 * curl localhost:5672
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins list
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management
 * service rabbitmq-server restart
 * http://rabbit3.dunnclan.net:15672/ guest/guest
 * yum -y install python-pika
 * git clone https://github.com/xiaodown/rabbitmq-quickdemo.git
 * send.py (a few times)
 * receive.py (let run) and then send.py again.
