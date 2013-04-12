import climatempo
import somar
import sms

if __name__ == '__main__':
	msgs = []

	m = climatempo.digest()
	if m is not None:
		msgs.append(m)

	m = somar.digest()
	if m is not None:
		msgs.append(m)

	sms.init()

	f = open('recipients', 'r')
	for num in f:
		for m in msgs:
			sms.send(num.strip(), m)
