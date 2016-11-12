# -*- coding: utf-8 -*-
import scrapy
from scrapy                                    import Selector
from scrapy.http                            import Request
from WordPress_Translation_Hack.items    import WordpressTranslationHackItem
# import pdb


class getStringsSpider(scrapy.Spider):
    name = "getStrings"
    allowed_domains = ["translate.wordpress.org"]
    
    start_urls = []


    def __init__ (self, toTranslate=None, translated=None, nameOfFile=None,*args, **kwargs):
        super( getStringsSpider, self).__init__(*args, **kwargs)
        #print( '\n'+str(toTranslate) )
        #print( str(translated) )

        self.start_urls = [ toTranslate ]
        self.translated = translated
        self.nameOfFile = nameOfFile if nameOfFile is not None else 'output.csv'

        self.untranslated = []
        self.Njourney = 0
        # self.translationReturn = []

    def parse(self, response):
    
        if self.Njourney is 0:
            
            nextUrl = self.stepOne(response)

            if nextUrl is not None:
                yield Request( nextUrl, callback=self.parse ) #recursive call 
            else:
                self.Njourney = 1
                yield Request( self.translated, callback=self.parse ) #recursive call 
            #     print ("----------------------")
            #     print ("end of the journey little hobbit")
            #     print ("----------------------")
            #     for x in self.untranslated:
            #         print ( x )
            #         print ("----------------------")
            #     print ( len( self.untranslated ) )
        elif self.Njourney is 1:

            nextUrl = self.stepTwo(response)
            
            if nextUrl is not None:
                yield Request( nextUrl, callback=self.parse ) #recursive call 
            else:
                print ("----------------------")
                print ("end of the journey little hobbit")
                print ("----------------------")
                # for x in self.translationReturn:
                #     print ( str(x) )
                #     print ("----------------------")
                # print ( "Old untranslated:" + str( len( self.untranslated ) ) +"\n Found: " + str( len( self.translationReturn ) ) ) 
                
                for r in self.untranslated:
                    yield r
                    
    # This will return the next url if exist
    # Search the untraslated
    def stepOne(self, response):
        
        hxs = Selector(response)
        # untranslatedRows = hxs.xpath('//table[@id="translations"]/tr[@class="preview untranslated priority-normal no-warnings"]/td[@class="original"]')
        untranslatedRows = hxs.xpath('//table[@id="translations"]/tr[ contains(@class, "untranslated") ]/td[@class="original"]')

        for rows in untranslatedRows:

            aux = WordpressTranslationHackItem()
            aux['originalString'] = ''

            for r in rows.xpath('./child::node()').extract():        
                aux['originalString'] = aux['originalString'] + r.strip() + ' '        
            
            self.untranslated.append( aux )
                
            # print ( self.untranslated[-1] )
            # print ( '------------------' )
            # pdb.set_trace()

        paginaSiguiente = []
        paginaSiguiente = hxs.xpath('//div[@class="paging"]/a[@class="next"]/@href')        

        try:            
            fullUrl_toNextPage = response.urljoin( paginaSiguiente[0].extract() )
            return fullUrl_toNextPage
        except Exception:
            return None

    # Search the translated that are not transalated in the stepOne
    def stepTwo(self, response):
        hxs = Selector(response)
        translatedRows = hxs.xpath('//table[@id="translations"]/tr[ contains(@class, "status-current") ]/td[@class="original"]')
       
        # print ( len(untranslatedRows) )
        # pdb.set_trace()

        for rows in translatedRows:

            aux = ""

            for r in rows.xpath('./child::node()').extract():        
                aux = aux + r.strip() + ' '        
            
            i = self.compareStrings(aux) 
            
            if i is not None:
                #scrapy item
                # traductionItem = W
                # traductionItem['originalString'] = aux
                self.untranslated[i]['translatedString'] = rows.xpath('./..//td[@class="translation foreign-text"]/text()').extract()[0].strip()
                
        paginaSiguiente = []
        paginaSiguiente = hxs.xpath('//div[@class="paging"]/a[@class="next"]/@href')

        try:            
            fullUrl_toNextPage = response.urljoin( paginaSiguiente[0].extract() )
            return fullUrl_toNextPage
        except Exception:
            return None

    def compareStrings(self, t):

        i = 0

        for x in self.untranslated:
            if t == x['originalString']:
                return i
            i += 1    
        
        return None