# -*- coding: utf-8 -*
import argparse
# import os

import scrapy
from scrapy.crawler import CrawlerProcess

from twisted.internet 				import reactor
from scrapy.crawler 				import Crawler
from scrapy.utils.project 			import get_project_settings

#--the spiders
from WordPress_Translation_Hack.spiders.getStrings import getStringsSpider
#--the spiders


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
parser.add_argument('-f','--file', metavar='"File-Name"',dest='file', required=False, help='Name of the CSV output file (Default = output.csv)')

args = parser.parse_args()

# -------------------------------------------
spider = getStringsSpider()
process = CrawlerProcess( get_project_settings() )

process.crawl(spider, toTranslate=args.toTranslate, translated=args.translated, nameOfFile=args.file )
process.start()
# -------------------------------------------