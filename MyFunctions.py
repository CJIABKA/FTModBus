#!/usr/bin/env python
# -*- coding: utf-8 -*-      
#from Transliterate import transliterate
#import re

def ReplaceCirilic(text):   
    if type(text) == str:
        text = text.decode('utf-8') 
    return text.replace(u'А', u'A').replace(u'В', u'B').replace(u'С', u'C').replace(u'Н', u'H').replace(u'Е', u'E').replace(u'К', u'K').replace(u'Х', u'X').replace(u'Р', u'P').replace(u'О', u'O').replace(u'М', u'M').replace(u'Т', u'T')


if __name__ == "__main__":
    pass
