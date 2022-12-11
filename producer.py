
def generate_events():
	# Python logging: NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40, and CRITICAL=50
	# from events import say_hellow
	import logging
	from redis import Redis
	import rq
	import sys

	logging.basicConfig(
		filename='/home/premkumarchalmeti/Documents/rq/producer_event.log', filemode='w', level=logging.DEBUG,
		datefmt='%d-%b-%y %H:%M:%S',
		format='%(asctime)s|%(funcName)s: %(lineno)d|%(levelname)s|%(message)s'
	)
	prod_logger = logging.getLogger('producer_email_logger')
	prod_logger.info('Hit')

	try:
		redis_conn = Redis('localhost', 6379)
		asynctask_q = rq.Queue('low', connection=redis_conn, is_async=True)
	except Exception:
		prod_logger.error('Connection error', exc_info=True)
		sys.exit(0)

	prod_logger.debug('Connection created')
	try:
		job = asynctask_q.enqueue('events.say_hellow', description='sample input', kwargs={
			'name': 'Premkumar',
			'description': 'Say hello to world',
			'ttl': 20
		})
	except Exception:
		prod_logger.error('Failed to enqueue task: %s' % job)
	prod_logger.debug('Task enqueued %s ' % job)

generate_events()
