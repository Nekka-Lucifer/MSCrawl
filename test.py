from stem import Signal
from stem.control import Controller
with Controller.from_port(address = '127.0.0.1', port = 9051) as controller:
	controller.authenticate(password='8obV16MqJgWc')
	controller.signal(Signal.NEWNYM)