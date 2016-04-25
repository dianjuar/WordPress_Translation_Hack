# -*- coding: utf-8 -*-
import scrapy
from scrapy             import Selector


class UntranslatedStringSpider(scrapy.Spider):
    name = "untranslated_String"
    allowed_domains = ["translate.wordpress.org"]
    start_urls = (
        'https://translate.wordpress.org/projects/wp/4.4.x/es-ve/default?filters[term]=&filters[user_login]=&filters[status]=untranslated&filter=Filter&sort[by]=priority&sort[how]=desc',
    )

    def __init__ (self):
    	self.untranslated = []

    def parse(self, response):

    	hxs = Selector(response)
    	untranslatedRows = hxs.xpath('//table[@id="translations"]/tr[@class="preview untranslated no-warnings priority-normal"]/td[@class="original"]')


    	for rows in untranslatedRows:

    		aux = ""

    		for r in rows.xpath('./child::node()').extract():    	
    			aux = aux + r.strip() + ' '		
			
    		self.untranslated.append( aux )
    			
    		print ( self.untranslated[-1] )
    		print ( '------------------' )

		# '''
  #   			

  #   	for row in untranslatedRows
  #   		print ('-------------------')
  #   		print ( str( row ) )
  #   		print ('-------------------')
		# '''
