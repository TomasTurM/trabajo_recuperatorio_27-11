import time

import redis
r = redis.Redis(host='localhost', port=6379)

def RedisPublisher():
	channel = input('Introduzca canal de Redis: ')
	channel = str(channel)
	print('Canal ' + channel)
	user_msg = input('Introduzca mensaje: ')
	user_msg = str(user_msg)
	frequency = input('Introduzca frecuencia en segundos: ')
	frequency = float(frequency)

	while True:
		r.publish(channel, user_msg)
		time.sleep(frequency)

RedisPublisher()