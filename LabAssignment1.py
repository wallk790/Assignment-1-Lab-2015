#!/usr/bin/env python

############## UNREAD TITLE SEARCH  ##############
## searches email titles and returns the summary of targetted search


#!/usr/bin/env python
# modified from http://elinux.org/RPi_Email_IP_On_Boot_Debian
# modified from Don Southard
import subprocess
import smtplib
import socket
import time
from email.mime.text import MIMEText
import datetime
import urllib2

import feedparser		# imports feedparser to parse XML feed

user='kwallace1994@gmail.com'		# replace dtclass15@gmail.com with your personal gmail user or email, or youruser@newschool.edu for your school account
passwd='landbeforetime94'		# replace *** with your password for the above account


newmails = feedparser.parse("https://" + user + ":" + passwd + "@mail.google.com/gmail/feed/atom").entries
for i in newmails:		#for loop itterates through newmails feed
    #print str(i.title)		# uncomment to print out each title of unread emails
    if str(i.title)=="Canvas":		# replace the word Search with the title of the email you are searching for
        print i.summary
        	###THIS MAY GO IN WHILE LOOP?? 


while True: 	#loop forever ---- to exit use keys "ctr+c"
    newmails1 = int(feedparser.parse("https://" + user + ":" + passwd + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
    
    def emailcount(n): #define function emailcount
        if n > 0: # if you have over 0 emails. You can change this based on how many emails you currently have unread in your inbox
            print "you have "+str(n)+" new email(s)"
        else: 
            print "you have no new email"

    emailcount(newmails1) #call emailcount function and pass value newmails as agrument
    time.sleep(60)		#wait 60 seconds




def sendEmail: 
# Change to your own account information
	to = 'kwallace1994@gmail.com'
	gmail_user = 'kwallace1994@gmail.com'
	gmail_password = 'landbeforetime94'
	smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_password)
	today = datetime.date.today()
	# Very Linux Specific
	arg='ip route list'
	p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
	data = p.communicate()
	split_data = data[0].split()
	ipaddr = split_data[split_data.index('src')+1]
	extipaddr = urllib2.urlopen("http://icanhazip.com").read()
	my_ip = 'Local address: %s\nExternal address: %s' %  (ipaddr, extipaddr)
	msg = MIMEText(my_ip)
	msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y') ###EDIT THIS FOR FUNCTION PORTION ?
	msg['From'] = gmail_user
	msg['To'] = to
	time.sleep(60)
	smtpserver.sendmail(gmail_user, [to], msg.as_string())
	smtpserver.quit()
