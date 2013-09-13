from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from Companies.items import CompaniesItem, LinkItem

class GetSpider(BaseSpider):
	name = 'Get'
	allowed_domains = ['masterseek.com']
	f = open("Get.txt")
	start_urls = [url.strip() for url in f.readlines()]
	f.close()
	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//div[@id="target_search"]/ul/li')
		items = []
		for site in sites:
			item = LinkItem()
			item['Link'] = site.select('p/a/@href').extract()
			items.append(item)
		return items

class ExtractSpider(BaseSpider):
	name = 'Extract'
	allowed_domains = ['masterseek.com']
	f = open("Links.txt")
	start_urls = [url.strip() for url in f.readlines()]
	f.close()
	try:
		start_urls[0] = "http://www.google.com"
	except:
		pass
	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		li = hxs.select('//ul[@id="company_details"]/li')
		i = CompaniesItem()
		i['CompanyName'] = li[1].select('h3/a/text()').extract()
		i['Website'] = li[1].select('h3/a/@href').extract()
		ps = li[2].select('p')
		i['Phone'] = ps[0].select('a/text()').extract()
		Address = str(ps[1].select('text()').extract()[0]).split(",")
		i['Address1'] = Address[0]
		i['Address2'] = Address[2]
		i['TownCity'] = Address[1]
		i['Postcode'] = Address[3]
		i['Category'] = ps[2].select('span/text()').extract()
		return i
