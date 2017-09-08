#!/usr/bin/env python3
#kopano backup v0.1 Basic functionality, webapp backup will be done one I can look into the new kopano backup
#V1.0 Changing name to Kopano Administration, implimenting email sends configs and much more features
import time
import argparse
from pathlib import Path
import kopano_func
options = argparse.ArgumentParser()
options.add_argument('-b', '--backup', help='Choose the backup you want to do: database or mailboxes')
options.add_argument('-r', '--restore', help='Restore the database, mailbox or file')
options.add_argument('-c', '--config', help='Choose to create or edit the exist config.')
options.parse_args()
program = options.parse_args()
if program.backup == "mailboxes":
    kopano_func.zarfallna()
else:
    kopano_func.database()

if program.restore == "database":
    kopano_func.resdatabase()
elif program.restore == "mailbox":
    kopano_func.resmailbox()
else:
    kopano_func.resfile()

if program.config == "create":
    kopano_func.confcreate()
else:
    kopano_func.confedit()
    

    

print("Welcome to Kopano Administration")
print("Checking if config exists")
config_check = Path("kopanoconfig")
if config_check.is_file():
    print("Config exists, will check arguments for specific functions")
else:
    print("Config does not exist, creating config")

print("Now checking arguments used")

    
    
    





