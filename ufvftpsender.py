from ftplib import FTP # base. fucking. functionality.
import sys # command line args
import re # ew
import json #interpreting headers

conf_file=sys.argv[1]
#checking the configuration file name.
if not bool(re.search(r"[a-zA-Z0-9]+\.json", conf_file)):
    print("CONFIGURATION FILE NAME NOT VALID!  \n PLEASE FOLLOW NAMING RULES. \n YOU DO NOT NEED TO BE QUIRKY.")

with open(conf_file, 'r') as f:
    data=json.load(f)
    # gets headers
    print(type(data))

ftp=FTP(data.get("reciever"))
ftp.login(user=data.get("username"), passwd=data.get("pwd"))
ftp.cwd(data.get("ufvftp dir"))

    
    
# early development comment spree alert frfrffrf!!!11!!