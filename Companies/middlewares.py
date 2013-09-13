from Companies.settings import USER_AGENT_LIST
import random
from stem import Signal
from stem.control import Controller
from scrapy import log

class RandomUserAgentMiddleware(object):
	def process_request(self, request, spider):
		ua  = random.choice(USER_AGENT_LIST)
		if ua:
			request.headers.setdefault('User-Agent', ua)
			log.msg('>>>> UA %s'%request.headers)
			
class ChangeProxyTorMiddleware(object):
	def process_response(self, request, response, spider):
		if ((response.status == 203) or (response.status == 403) or (response.status == 503)):
			log.msg('203/403/503 Error found')
			with Controller.from_port(address = '127.0.0.1', port = 9051) as controller:
				controller.authenticate(password='8obV16MqJgWc')
				controller.signal(Signal.NEWNYM)
				log.msg('Using new identity')
				return request
		return response