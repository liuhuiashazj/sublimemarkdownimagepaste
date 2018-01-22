
from richxerox import *
import os
import re
pasteType=available()[0]
print(pasteType)

def getClipboadContent(o_type):
    _type=''
    _out=''
    if(o_type.find('.png')!=-1):
        _type='image'
        _out=''

    elif(o_type.find('html')!=-1||o_type.find('text')!=-1):
        _type='html'
        _out=paste(format='html')

    elif(o_type.find('rtf')!=-1):
    	_type='rtf'
    	_out=paste(  format='rtf')
    res={
        '_type':_type,
        '_out':_out
    }
    return res

content=getClipboadContent(pasteType)
#print(paste(format='text'))
#print(paste(format='html'))
print(content)




