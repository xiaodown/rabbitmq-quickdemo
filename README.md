rabbitmq-quickdemo
==================

prior to demo:

 * yum install git vim 
 * su -c 'rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm' (?may already be done)

Commands for to make demo:

 * yum install rabbitmq-server -y
 * service iptables stop
 * service rabbitmq-server start
 * curl localhost:5672
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins list
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management
 * service rabbitmq-server restart
 * http://the.hostname.or.IP:15672/ guest/guest
 * yum -y install python-pika
 * git clone https://github.com/xiaodown/rabbitmq-quickdemo.git
 * send.py (a few times)
 * receive.py (let run) and then send.py again.
