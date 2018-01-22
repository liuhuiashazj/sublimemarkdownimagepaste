import sys 
import os
import re
import sublime, sublime_plugin
from . import syspath
from .getImageName import random_str
from .setting import image_abs_path
from os.path import relpath


def getPythonPath(pyname):
    plugin_path = sublime.packages_path()
    plugin_path = re.sub(r'\s', "\ ", plugin_path)+'/copyimagetomarkdown/'
    #python shell
    ppath=plugin_path+pyname
    return ppath;
def getSetting():
    history_filename = 'copyimagetomarkdown.sublime-settings'
    history = sublime.load_settings(history_filename)
    image_abs_path = history.get("imageAbsolutePath")
    return image_abs_path

# ExampleCommand名字中Command为必须的
# ExampleCommand将会转换成下划线风格example，又例如TortoiseSaveCommand会变成tortoise_save
class CopyToMarkdownCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        #fname = sublime.get_clipboard()
        #reg=sublime.Region(0,10)
        
        variable=self.view.window().extract_variables()
        file_name=variable['file_name']
        image_name=file_name+random_str()+'.png'
        absPathPython=getPythonPath('pasteImg.py')
        image_abs_path=getSetting()
        pshell_arg='python '+absPathPython+' '+image_abs_path+' '+image_name
        copy_result = os.popen(pshell_arg).read()


        print('start')
        print(copy_result)
        print('end')
        file_path=variable['file_path']
        file_base_name=variable['file_base_name']
        imageRelPath=os.path.relpath(image_abs_path,file_path)
        image_base_name=imageRelPath+'/'+image_name
        self.view.insert(edit, self.view.sel()[0].begin(), '![]('+image_base_name+')\n')





    