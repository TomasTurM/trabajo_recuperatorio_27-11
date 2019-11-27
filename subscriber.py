import redis
r = redis.Redis(host='localhost', port=6379)

def RedisSuscriber():
	sub = r.pubsub()
	sub.subscribe('alpha')
	print('Conectado al canal alpha')

	while True:
		msg = sub.get_message()

		if msg:
			to_print = msg['data']
			print(to_print)

RedisSuscriber()