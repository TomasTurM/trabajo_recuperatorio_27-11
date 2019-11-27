import time

import redis
r = redis.Redis(host='localhost', port=6379)

def RedisPublisher():
	print('Canal alpha')
	user_msg = input('Introduzca mensaje: ')
	user_msg = str(user_msg)
	frequency = input('Introduzca frecuencia en segundos: ')
	frequency = float(frequency)

	while True:
		r.publish('alpha', user_msg)
		time.sleep(frequency)

RedisPublisher()