#!/bin/bash
echo "hi Global"
echo 'Username: ' $1  && echo 'Directory: ' $2
username="$1"
dirpath="$2"
if [ $username = "root" ];
then 
 echo "Finding root user data is not allowed!"
 exit 42
else
 find $dirpath -type f -user $username 
 ps -u $username -o pid,user,cmd
fi
