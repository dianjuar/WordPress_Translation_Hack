# -*- coding: utf-8 -*
import argparse
import os

#import scrapy
#from scrapy.crawler import CrawlerProcess
from WordPress_Translation_Hack.spiders.getStrings import getStringsSpider

'''
Una herramienta para traducir 
WordPress más rápidamente basandose 
en strings traducidos de otros 
idiomas.
'''

des='''\
     WordPress          Translation            Hack
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |  _________   | || |  ____  ____  | |
| ||_   _||_   _|| || | |  _   _  |  | || | |_   ||   _| | |
| |  | | /\ | |  | || | |_/ | | \_|  | || |   | |__| |   | |
| |  | |/  \| |  | || |     | |      | || |   |  __  |   | |
| |  |   /\   |  | || |    _| |_     | || |  _| |  | |_  | |
| |  |__/  \__|  | || |   |_____|    | || | |____||____| | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
     WordPress          Translation            Hack
-------------------------------------------------------------
----------------------Description-----------------------------

A tool to hack WordPress Translation at 
https://translate.wordpress.org.

This tool will search which strings are not translated 
and search the corresponding translation on another language 
already translated, generating after the execution a CSV file
with the missing string in it.

With this you will be faster and effective. Every one can 
copy an paste.
----------------------Parameters-----------------------------
'''
epi='''\
------------------------WARNING!-----------------------------
I recomend know read the entire string and translate it 
in your mind in case that contains an error or don't 
adjust to your local lenguage.

Mantein the web is the jobs of all of us.
'''

parser = argparse.ArgumentParser(
	prog='WordPress Translation Hack',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=des,
    epilog=epi)


#toTranslate
#parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('-d','--to-translate', metavar='"Web-Page"', dest='toTranslate', required=True, help='The web page when are the strings TO BE translated')
parser.add_argument('-o','--translated', metavar='"Web-Page"', dest='translated', required=True, help='The web page when are the strings TRANSLATED')
parser.add_argument('-f','--file', metavar='"File-Name"', dest='file', required=True, help='Name of the CSV output file')

args = parser.parse_args()

os.system( 'scrapy crawl getStrin -a toTranslate='+args.toTranslate+' -a translated='+args.translated+' -o '+ args.file +' -t csv' )

#spider = getStringsSpider(toTranslate=str(args.toTranslate), translated=str(args.translated) )
#process = CrawlerProcess({
#    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#})
#
#process.crawl(spider, args.toTranslate)
#process.start()
#os.system('scrapy crawl getStrings -a toTranslate='+args.toTranslate+' -a translated='+args.translated)