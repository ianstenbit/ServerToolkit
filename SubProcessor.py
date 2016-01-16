import subprocess
import os

class SubProcessor():
    
    def __init__(self, cwd):
        self.cwd = cwd
        self.users = {"3038153710@mms.att.net": "hackrice2016"}
        self.authorized = False

    def authorize(self, user, password):
        correct_pw = ""
        try:
            correct_pw = self.users[user]
            if correct_pw == password:
                self.authorized = True
                return "Authorization success."
            else:
                return "Authorization failed. Try again."
        except KeyError:
            return "Authorization failed. Try again."

        
    def run(self, command):
        if (not self.authorized):
            return "Server access not authorized."
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
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True);
        except subprocess.CalledProcessError as e:
            output = e.output

        # change directory if necessary
        if (dirChanged):
            self.cwd = output.strip()
        return output
