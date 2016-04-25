# -*- coding: utf-8 -*-
import scrapy
from scrapy            						import Selector
from scrapy.http        					import Request
from WordPress_Translation_NewToOld.items	import WordpressTranslationNewtooldItem


class UntranslatedStringSpider(scrapy.Spider):
    name = "untranslated_String"
    allowed_domains = ["translate.wordpress.org"]
    start_urls = (
        'https://translate.wordpress.org/projects/wp/4.4.x/es-ve/default?filters[term]=&filters[user_login]=&filters[status]=untranslated&filter=Filter&sort[by]=priority&sort[how]=desc',
        
    )

    def __init__ (self):
    	self.untranslated = []
    	self.Njourney = 0
    	self.translationReturn = []

    def parse(self, response):
    
    	if self.Njourney is 0:
    		
    		nextUrl = self.stepOne(response)

    		if nextUrl is not None:
	    		yield Request( nextUrl, callback=self.parse ) #recursive call 
	    	else:
	    		self.Njourney = 1
	    		yield Request( "https://translate.wordpress.org/projects/wp/dev/es-ve/default?page=1", callback=self.parse ) #recursive call 
	    	# 	print ("----------------------")
	    	# 	print ("end of the journey little hobbit")
	    	# 	print ("----------------------")
	    	# 	for x in self.untranslated:
	    	# 		print ( x )
	    	# 		print ("----------------------")
	    	# 	print ( len( self.untranslated ) )
    	elif self.Njourney is 1:

    		nextUrl = self.stepTwo(response)
    		
    		if nextUrl is not None:
	    		yield Request( nextUrl, callback=self.parse ) #recursive call 
	    	else:
	    		print ("----------------------")
	    		print ("end of the journey little hobbit")
	    		print ("----------------------")
	    		# for x in self.translationReturn:
	    		# 	print ( str(x) )
	    		# 	print ("----------------------")
	    		print ( "Old untranslated:" + str( len( self.untranslated ) ) +"\n Found: " + str( len( self.translationReturn ) ) ) 
	    		
	    		for r in self.translationReturn:
	    			yield r
    	

    #this will return the next url if exist
    def stepOne(self, response):
    	
    	hxs = Selector(response)
    	untranslatedRows = hxs.xpath('//table[@id="translations"]/tr[@class="preview untranslated no-warnings priority-normal"]/td[@class="original"]')


    	for rows in untranslatedRows:

    		aux = ""

    		for r in rows.xpath('./child::node()').extract():    	
    			aux = aux + r.strip() + ' '		
			
    		self.untranslated.append( aux )
    			
    		# print ( self.untranslated[-1] )
    		# print ( '------------------' )

    	paginaSiguiente = []
    	paginaSiguiente = hxs.xpath('//div[@class="paging"]/a[@class="next"]/@href')    	

    	try:    		
    		fullUrl_toNextPage = response.urljoin( paginaSiguiente[0].extract() )
    		return fullUrl_toNextPage
    	except Exception:
    		return None

    def stepTwo(self, response):
    	hxs = Selector(response)
    	translatedRows = hxs.xpath('//table[@id="translations"]/tr[@class="preview status-current no-warnings priority-normal"]/td[@class="original"]')

    	for rows in translatedRows:

    		aux = ""

    		for r in rows.xpath('./child::node()').extract():    	
    			aux = aux + r.strip() + ' '		
			
    		if self.compareStrings(aux):
	    		traductionItem = WordpressTranslationNewtooldItem()
	    		traductionItem['originalString'] = aux
	    		traductionItem['translatedString'] = rows.xpath('./..//td[@class="translation foreign-text"]/text()').extract()
	    		self.translationReturn.append( traductionItem )

    	paginaSiguiente = []
    	paginaSiguiente = hxs.xpath('//div[@class="paging"]/a[@class="next"]/@href')

    	try:    		
    		fullUrl_toNextPage = response.urljoin( paginaSiguiente[0].extract() )
    		return fullUrl_toNextPage
    	except Exception:
    		return None

    def compareStrings(self, t):

    	if t in self.untranslated:
    		return True
    	
    	return False
