import redis
r = redis.Redis(host='localhost', port=6379)

def RedisSuscriber():
	channel = input('Introduzca canal de Redis a escuchar: ')
	channel = str(channel)
	print('Canal ' + channel)
	sub = r.pubsub()
	sub.subscribe(channel)
	print('Conectado al canal ' + channel)

	while True:
		msg = sub.get_message()

		if msg:
			to_print = msg['data']
			print(to_print)

RedisSuscriber()