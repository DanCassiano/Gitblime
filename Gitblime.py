import sublime, sublime_plugin
import subprocess 


class GitblimeCommand(sublime_plugin.TextCommand):

	r = None

	def run(self, edit):			
		self.showPainel( self.gitStatus() );
		# print(self.gitStatus())

	def showPainel( self, dados ):
		self.window = self.view.window()
		output = self.window.create_output_panel("consulta")
		
		output.run_command('erase_view')
		output.run_command('append', {'characters': dados})
		output.set_syntax_file("Packages/Markdown/Markdown.tmLanguage")

		self.window.run_command("show_panel", {"panel": "output.consulta"})

	def gitStatus(self):
		self.r = subprocess.check_output(["git", "status", "-s"], stderr=subprocess.STDOUT)
		return str(self.r, encoding='utf8')
