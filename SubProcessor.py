import subprocess
import os

class SubProcessor():
    
    def __init__(self, cwd):
        self.cwd = cwd
        
    def run(self, command):
        # change directory to current (as defined by previously executed commands)
        os.chdir(self.cwd)

        # handle different types of commands
        args = command.split(" ")
        dirChanged = False
        if (args[0] == "cd"):
            command += "; pwd"
            dirChanged = True

        # handle incorrect commands
        try: 
            output = subprocess.check_output(command, shell=True);
        except subprocess.CalledProcessError as e:
            output = e.output

        # change directory if necessary
        if (dirChanged):
            self.cwd = output.strip()
        return output