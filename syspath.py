import sys 
import os

new_pa='/usr/local/lib/python3.5/site-packages/'
new_pa1='/Users/liuhui/Library/Application Support/Sublime Text 3/Packages/copyimagetomarkdown/site-packages'
new_pa2='/Library/Python/2.7/site-packages'
new_pa3='/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python'
def AddSysPath(new_path):  
    new_path = os.path.abspath(new_path)
    for x in sys.path:  
        if new_path in (x, x + os.sep):  
            return 0  
    sys.path.append(new_path)

def RemoveSysPath(new_path):
    new_path = os.path.abspath(new_path)
    for x in sys.path:  
        if new_path in (x, x + os.sep):  
            sys.path.remove(new_path)  

RemoveSysPath(new_pa)
RemoveSysPath(new_pa2)
RemoveSysPath(new_pa3)
#RemoveSysPath(new_pa3)
#AddSysPath(new_pa) 
#AddSysPath(new_pa1) 
#AddSysPath(new_pa) 
#AddSysPath(new_pa3) 
