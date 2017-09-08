#!/usr/bin/env python3
#kopano functions
import os
import configparser
import time
from subprocess import call
def confcreate():
    print("Welcome to the config creator!")
    print("We will go by step, by step questions you will need to answer, at the end of the config creation you can choose to edit a section again")    
    def mailserv():
        mail_hostname = input("What is the hostname of the server you're sending from? ")
        mail_port = input("Please type the port of the server ")
        mail_ssl_confirm = input("Does server use encryption? (yes or no) ").lower()
        if mail_ssl_confirm == "yes":
            mail_ssl_type = input("Please choose from the following 1) SSL 2) TLS 3) STARTTLS ")
            if mail_ssl_type == "1":
                print("Encryption type {} chosen, next question".format(mail_ssl_type))
                mail_ssl = ssl
            elif mail_ssl_type == "2":
                print("Encryption type {} chosen, next question".format(mail_ssl_type))
                mail_ssl = tls
            elif mail_ssl_type == "3":
                print("Encryption type {} chosen, next question".format(mail_ssl_type))
                mail_ssl = starttls
        else:
            mail_ssl = []
            print("Confirmed no encryption continuing")
        mail_auth_confirm = input("Does your server require authentication? ").lower()
        if mail_auth_confirm == "yes":
            mail_auth_usn = input("What is the username for the smtp server? ")
            mail_auth_pw = input("Please type the password for the smtp server: ")
        else:
            mail_auth_usn = []
            mail_auth_pw = []
            print("Confirmed no authentication required, continuing")
        mail_from_address = input("Please put in the mail from address: ")
        mail_to_address = input("Please put in the mail to address: ")
        
    
def zarfallna():
      
    des = input("Please state the backup location? ")
    print ("You have decided to back up to {}".format(des))
    change = input("Do you want to change the backup destination?  (yes or no)")
    if change == "yes":
        des = input("please state the backup location? ")
        print ("You have decided to back up to {}".format(des))
        change = input ("Do you want to change the backup destionation (yes or no)")
    else:
        print("Starting the backup!")
    
    runbk = ['zarafa-backup', '-avo', des, '>', '/var/log/zbackuplog-$(date +%Y-%m-%d-%h-%M).log']
    print("starting backup {}".format(runbk))
    call(runbk)
    print("Backup is now complete")
     
def zrestorena():
    print("This is the non automated restore function")
    print("You can use this to restore whole mailboxes or individual items, going through the steps")
    print("If you know what you want to restore straight away please use the automated function, see help for commands")
    restore = input("What type of backup restoration you want to do? (mailbox/item)")
    if restore == "mailbox":
        bkloc = input("Where are the backups located? Please specify the full path with a / at the end")
        bklochge = input("Is this the correct path? (yes or no)")
        if bklochge == "no":
            bkloc = input("Where are the backups located? Please specify the full path")
            bklochge = input("Is this the correct path? (yes or no)")
        else:
            print("Backup location has been confirmed as {}".format(bkloc))
            
        usermb = input("What's the username of the person you want the mailbox restored of? ")
        userch = input("The user you stated is {} is this correct? (yes or no) ".format(usermb))
        if userch == "no":
            usermb = input("What's the username of the person you want the mailbox restored of? ")
            userch = input("The user you stated is {} is this correct? (yes or no) ".format(usermb))
        else:
            print("Confirmed user {} now we need to confirm the user to restore to".format(usermb))
        restoreuser = input("Is the user you want to restore the mailbox of the same user you want to restore the mailbox to? (yes or no)")
        if restoreuser == "no":
            resuser = input("Please type the username of the person you want to restore the mailbox to?")
            conres = input("You have stated {} is this correct? (yes or no)".format(resuser))
        elif conres == "no":
            resuser = input("Please type the username of the person you want to restore the mailbox to?")
            conres = input("You have stated {} is this correct? (yes or no)".format(resuser))
        else:
            print("Confirmed the user is {} proceeding to backup".format(resuser))
        
        runbk = [ 'cd', bkloc, ';', '/usr/share/zarafa-backup/full-restore.sh', usermb, resuser]
        print("Starting backup {}".format(runbk))
        call(runbk)
        print("Restoring is complete")       
            
    else:
        print("Individual files chosen, proceeding backup")
        bkloc = input("Where are the backups located? Please specify the full path with a / at the end")
        bklochge = input("Is this the correct path? (yes or no)")
        if bklochge == "no":
            bkloc = input("Where are the backups located? Please specify the full path")
            bklochge = input("Is this the correct path? (yes or no)")
        else:
            print("Backup location has been confirmed as {}".format(bkloc))
            
        usermb = input("What's the username of the person you want the file restored of? ")
        userch = input("The user you stated is {} is this correct? (yes or no) ".format(usermb))
        if userch == "no":
            usermb = input("What's the username of the person you want the file restored of? ")
            userch = input("The user you stated is {} is this correct? (yes or no) ".format(usermb))
        else:
            print("Confirmed user {} now we need to confirm the user to restore to".format(usermb))
        while True:
            options = input("Choose from the following a = list files in backup, b = restore file, c = quit backup")
            if options == "a":
                print("Gathering data, please take a note of the unique ID of the item you want to restore then when requested put it into the backup to restore items")
                usermb = usermb.index.zbk
                lsfls = [ 'cd', bkloc, ';', '/usr/share/zarafa-backup/readable-index.pl', usermb, ' | less' ]
                call(lsfls)
                continue
            if options == "b":
                zaid = input("Please put in the unique ID of the item you want to restore")
                cfch = input("Is this the correct id? yes or no {}".format(zaid))
                if cfch == "no":
                    zaid = input("Please put in the unique ID of the item you want to restore")
                else:
                    print("We will now restore the item")
                    rsit = [ 'cd', bkloc, ';', 'zarafa-restore -r -u', usermb, zaid]
                    call(rsit)
                    print("File has now been restored")
                continue
            if options == "c":
                break
             
            
                