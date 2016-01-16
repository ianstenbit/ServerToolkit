import subprocess
import os

class SubProcessor():
    
    def __init__(self, cwd):
        self.cwd = cwd
        
    def run(self, command):
        os.chdir(self.cwd)
        args = command.split(" ")
        needShell = False
        dirChanged = False
        if (args[0] == "cd"):
            command += "; dirs -l"
            needShell = True
            dirChanged = True
        output = subprocess.check_output(command, shell=needShell);
        if (dirChanged):
            self.cwd = output.strip()
        return output


