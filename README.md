![WordPress Translation Hack](http://i.imgur.com/4mUFw5S.png)

## Description
A tool to hack WordPress Translation at 
https://translate.wordpress.org.

This tool will search which strings are not translated and search the corresponding translation on another language  already translated, generating after the execution a CSV file with the missing string in it.

With this you will be faster and effective. Every one can copy an paste.

## Usage
```
usage: WordPress Translation Hack [-h] -d URL-UNtranslated -o
                                  URL-translated [-f File-Name]
```    
### Parameters
```
optional arguments:
  -h, --help            show this help message and exit
  -d "Web-Page", --to-translate "Web-Page"
                        The web page when are the strings TO BE translated
  -o "Web-Page", --translated "Web-Page"
                        The web page when are the strings TRANSLATED
  -f "File-Name", --file "File-Name"
                        Name of the CSV output file (Default = output.csv
```

## Dependencies 
- scrapy
- argparse
	### Installing Dependencies
    
    - #### If your default python is *python 2.7*
          pip install scrapy
          pip install argparse    
    - #### If your default python is *python 3.5*
          pip2 install scrapy
          pip2 install argparse

## Recomendation
I recomend know read the entire string and translate it 
in your mind in case that contains an error or don't 
adjust to your local lenguage.

Mantein the web is the jobs of all of us.
