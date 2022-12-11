from redis import Redis
from events import generate_report, send_report
import rq

redis_conn = Redis('localhost', 6379)

task_q = rq.Queue('medium', connection=redis_conn)

report_gen_job = task_q.enqueue(generate_report)

print report_gen_job.result

task_q.enqueue(
	send_report, 
	kwargs=dict(report=report_gen_job.result), 
	depends_on=report_gen_job
)
