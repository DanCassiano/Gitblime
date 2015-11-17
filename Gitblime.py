import sublime, sublime_plugin
import subprocess 
from subprocess import Popen, PIPE
import os
import re
import sys


if sublime.platform() != 'windows':
	import pwd


class GitblimeCommand(sublime_plugin.TextCommand):

	r = None

	def run(self, edit):			
		# self.showPainel( self.gitLogBunito() );
		p = subprocess.Popen( "git status", cwd="C:/wamp/www/app/", shell=True, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate()
		self.showPainel(str(stdout, encoding='utf8'))
		

	def showPainel( self, dados ):
		self.window = self.view.window()
		output = self.window.create_output_panel("consulta")
		
		output.run_command('erase_view')
		output.run_command('append', {'characters': dados})
		output.set_syntax_file("Packages/Markdown/Markdown.tmLanguage")

		self.window.run_command("show_panel", {"panel": "output.consulta"})

	def gitStatus(self):
		self.r = subprocess.check_output( "git status" , cwd="C:/wamp/www/app/", shell = True)
		return str(self.r, encoding='utf8')

	def gitLogBunito(self):
		self.r = subprocess.check_output(["git","log", '--pretty=format:commit=%H,commithash=%h,autor=%an,datarelativa=%ar,autordata=%at,autoremail=%ae,commitername=%cn,msg=%s+'])
		return str(self.r, encoding='utf8')

	def getTotalCommit(self):		
		self.r = subprocess.check_output("cmd git log ", shell=True)
		retorno = str(self.r, encoding='utf8').split(';')
		return len(retorno)
	
	def get_subl_executable_path( self ):
		"""Return the path to the subl command line binary."""
		executable_path = sublime.executable_path()

		if sublime.platform() == 'osx':
			suffix = '.app/'
			app_path = executable_path[:executable_path.rfind(suffix) + len(suffix)]
			executable_path = app_path + 'Contents/SharedSupport/bin/subl'

		return executable_path
