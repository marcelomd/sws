# coding=utf-8

from humansms.service.SimpleMessageService import SimpleMessageService

__user = None
__password = None

def init():
	global __user
	global __password
	f = open('zenvia', 'r')
	__user = f.readline().strip()
	__password = f.readline().strip()
	f.close()

def send(to, msg):
	print('Sending to %s:' % to)

	if len(msg) > 150:
		print('Message too long (%d)' % len(msg))
		return

	send = SimpleMessageService(__user, __password)
	rc = send.sendSimpleMsg(msg, to)
	for r in rc:
		print(to + ': ' + r.getCode() + ' - ' + r.getDescription())
