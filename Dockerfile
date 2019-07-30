FROM rabbitmq:3.7-management

RUN rabbitmq-plugins enable rabbitmq_mqtt

EXPOSE 1883