#!/usr/bin/env python

from sys import argv
import subprocess
def showinfo():
    username=argv[1]
    dirpath=argv[2]

    print (f'Username: {argv[1]}', f'Directory: {argv[2]}')

    if username == "root":
        print ("Finding root user data is not allowed!")
        subprocess.run(['exit 42'],shell=True)
    else:
        subprocess.run([f'find {dirpath} -type f -user {username}'],shell=True)
        subprocess.run([f'ps -u{username} -o pid,user,cmd'],shell=True)

showinfo()

