import sublime, sublime_plugin
history_filename = 'copyimagetomarkdown.sublime-settings'
history = sublime.load_settings(history_filename)
image_abs_path = history.get("imageAbsolutePath")
#print(imageAbsolutePath)