import subprocess
import os

class SubProcessor():

	def __init__(self, cwd):
		self.cwd = cwd

	def run(self, command):
		args = command.split(" ")
		needShell = False
		if (args[0] == "cd"):
			command += "; dirs"
			needShell = True
		return subprocess.check_output(command, shell=needShell);


