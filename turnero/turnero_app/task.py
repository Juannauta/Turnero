
import time
import redis
import os
import json
from config import celery_app
redis_client = redis.StrictRedis(host=os.environ.get('REDIS_SERVER_HOST'), port=6379, db=0)



@celery_app.task()
def task_notification(pk=None):
    """
    the request is very fast and the database does not send answer for this is used sleep
    """
    data = json.dumps({"recargar":"{}".format(pk)})
    redis_client.publish('nuevo_turno', data)