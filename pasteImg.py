import sys
from PIL import ImageGrab

from richxerox import *
import os
import re
pasteType=available()[0]

def getClipboadContent(o_type):
    _type=''
    _out=''
    print(o_type.find('.png')!=-1)
    if(o_type.find('.png')!=-1):
        _type='image'
        _out=''
        saveImg()
    elif(o_type.find('text')!=-1):
        _type='text'
        _out=paste(format='text')
    elif(o_type.find('html')!=-1):
        _type='html'
        _out=paste(format='html')
    elif(o_type.find('rtf')!=-1):
    	_type='rtf'
    	_out=paste(format='rtf')
    res={
        '_type':_type,
        '_out':_out
    }
    return res


def saveImg():
	ImagePath=sys.argv[1]
	ImageName=sys.argv[2]
	
	# print('start to paste Image')
	im = ImageGrab.grabclipboard()
	im.save(ImagePath+'/'+ImageName,'PNG')
	# print('success to paste Image')

saveImg()

content=getClipboadContent(pasteType)
print(content)
