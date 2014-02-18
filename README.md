rabbitmq-quickdemo
==================

prior to demo:

 * yum install git vim 
 * su -c 'rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm' (?may already be done)

Commands to set up rabbitmq:

 * yum install rabbitmq-server -y
 * service iptables stop
 * service rabbitmq-server start
 * curl localhost:5672
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins list
 * /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management
 * service rabbitmq-server restart
 * http://<hostname|IP>:15672/ guest/guest
 * yum -y install python-pika
 * git clone git@github.com:xiaodown/rabbitmq-quickdemo.git
