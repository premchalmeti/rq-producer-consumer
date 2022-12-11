from redis import Redis
from rq.decorators import job
import time


redis_conn = Redis('localhost', 6379)

@job('low', connection=redis_conn, timeout=5)
def add(x, y):
	return x + y


job = add.delay(3, 4)
time.sleep(4)
print(job.result)
