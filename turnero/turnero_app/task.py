
import time
import redis
import os
from config import celery_app
redis_client = redis.StrictRedis(host=os.environ.get('REDIS_SERVER_HOST'), port=6379, db=0)



@celery_app.task()
def task_notification(pk=None):
    """
    the request is very fast and the database does not send answer for this is used sleep
    """
    redis_client.publish('nuevo_turno', '{"recargar":"{}"}'.format(pk))
    print("publique")
