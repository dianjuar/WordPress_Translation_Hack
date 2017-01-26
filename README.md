#WordPress Translation Hack

## Description
A tool to hack WordPress Translation at 
https://translate.wordpress.org.

This tool will search which strings are not translated and search the corresponding translation on another language  already translated, generating after the execution a CSV file with the missing string in it.

With this you will be faster and effective. Every one can copy an paste.

## Usage
> Only compatible with python2.7

```bash
python WordPressTranslationHack.py -d URL-UNtranslated -o URL-translated [-f File-Name.csv]
```

### Arguments
```
-h,             --help            
    show help message and exit

-d "URL",  --to-translate "URL"
    The web page when are the strings TO BE translated

-o "URL",  --translated "URL"
    The web page when are the strings TRANSLATED

-f "File-Name", --file "File-Name"
    Name of the CSV output file (Default = output.csv)
```

## Installation Guide.
### Using Python Virtual Environment (**Recommended**)

> We recommend use virtual environments because is much easier and your system won't install libraries that you don't commonly use. 
You forget a lot of the compatibility problems between python2 and python3.

1. Install [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) in your system
2. Clone this Repo.
3. Step into the just cloned repo folder
2. Create a Virtual Environment with python2.7 as default, using **`virtualenv -p /usr/bin/python2.7 YOUR_VIRTUAL_ENV_NAME`** for **linux** users
3. Open your virtual environment using **`source YOUR_VIRTUAL_ENV_NAME/bin/activate`**
4. Install the project dependencies with **`pip install scrapy`** and **```pip install argparse```**
5. **You are ready to run!.** _Every time you want the WTH you need to open your virtual environment._

## Recommendation
I recommend read the entire string and translate it in your mind in case that contains an error or don't adjust to your local language before submit it.

## Demonstration
[![Demonstrative video](http://i.imgur.com/fENtbEy.png)](https://youtu.be/LEp6NQ5F-RQ)

---------------

> Written with [StackEdit](https://stackedit.io/).

