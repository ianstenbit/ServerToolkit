This is a program which allows you to remotely control your home computer or server using SMS messages in a format which we call 'SSh over SMS'. It features two factor authentication using a password stored in the config.txt file.
To use for yourself:
- Build a dummy gmail account
- Download this repository
- Edit the time in time.sleep() at the bottom of PyMail.py to specify how long you want the program to run for. (On my server it's set up as an hourly cronjob so I run it for one hour at a time)
- Edit the config file to include in this order:
1) your gmail account address
2) your gmail account password
3) the email associated with your phone number (google "email over sms" to find the extension for your carrier)
4) the password used for two-factor authentication

The contact info in the current config.txt file is fake. 
Do not try to contact the email or phone number in the config file.

Link to a video demo: https://devpost.com/software/ssh-over-sms
