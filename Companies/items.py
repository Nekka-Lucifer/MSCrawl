# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CompaniesItem(Item):
	# define the fields for your item here like:
	# name = Field()
	CompanyName = Field()
	Category = Field()
	Phone = Field()
	Address1 = Field()
	Address2 = Field()
	TownCity = Field()
	Postcode = Field()
	Website = Field()
	#Updated = Field()
	pass

class LinkItem(Item):
	Link = Field()
	pass
