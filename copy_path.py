import sublime, sublime_plugin
import os.path

class CopyPathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.file_name()) > 0:
            sublime.set_clipboard(self.view.file_name())
            sublime.status_message("Copied full file path")

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0

class CopyFileNameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	full_name = self.view.file_name()
    	folder_name, file_name = os.path.split(full_name)
        if len(self.view.file_name()) > 0:
            sublime.set_clipboard(file_name)

            sublime.status_message("Copied file name")

class CopyPathOfFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	full_name = self.view.file_name()
    	folder_name, file_name = os.path.split(full_name)
        if len(self.view.file_name()) > 0:
            sublime.set_clipboard(folder_name)

            sublime.status_message("Copied path of file")

