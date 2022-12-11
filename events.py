
def say_hellow(name, description, ttl):
	msg = 'Hello %s!, %s' % (name, description)
	log_file = open('event.log', 'w+')
	log_file.write(msg)
	log_file.close()
	print msg
	return msg


def generate_report():
	from datetime import datetime
	report = open('report_%s.csv' % datetime.now(), 'w')
	report.write('%s: 21 days not logged in user: %s\n' % 
		(datetime.now(), 560)
	)
	report.close()

	msg = '%s' % report.name

	print msg
	return msg


def send_report(report):
	print report
	report = open(report, 'r')

	msg = 'Read %s: \nData:\n'.join(report.readlines())

	print msg
	return msg
