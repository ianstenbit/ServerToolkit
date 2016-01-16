import subprocess
import os

class SubProcessor():
    
    def __init__(self, cwd):
        self.cwd = cwd
        try:
            config = open('config.txt', 'r')
            print config.readline().strip()
            print config.readline().strip()
            usr = config.readline().strip()
            print usr
            pss = config.readline().strip()
            print pss
            self.users = {usr: pss}
        except IOError:
            print "IOError - no config file"
        self.authorized = False

    def authorize(self, user, password):
        correct_pw = ""
        try:
            password = password.strip()
            user = user.strip()

            print password
            print user

            print self.users

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
            #command += "; pwd"
            dirChanged = True

        # handle incorrect commands
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True);
        except subprocess.CalledProcessError as e:
            output = e.output.replace(":", "")
            dirChanged = False

        # change directory if necessary
        if (dirChanged):
            self.cwd = subprocess.check_output(command+"; pwd", shell=True).strip()
        return output
