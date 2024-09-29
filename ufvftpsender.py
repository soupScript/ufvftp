from ftplib import FTP # base. fucking. functionality.
import sys # command line args
import re # ew
import json #interpreting headers
import subprocess #running shell code
import threading #other base functionality ig?
import os # make temp directory
import shutil #remove directory
#for theading
threadvar=[]
conf_file=sys.argv[1]
input_file=sys.argv[2]

#makes temportary file for files
os.makedirs("temp", exist_ok=True)
command=f"ffmpeg -i {input_file} -c copy -map 0 -segment_time 1 -f segment temp/output%05d.mp4"
result=subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
#checking the configuration file name.
if not bool(re.search(r"[a-zA-Z0-9]+\.json", conf_file)):
    print("CONFIGURATION FILE NAME NOT VALID!  \n PLEASE FOLLOW NAMING RULES. \n YOU DO NOT NEED TO BE QUIRKY.")

with open(conf_file, 'r') as f:
    data=json.load(f)
    # gets headers
    print(type(data))


def uploadfile(name):
    ftp=FTP(data.get("reciever"), data.get("port"))
    ftp.login(user=data.get("username"), passwd=data.get("pwd"))
    ftp.cwd(data.get("ufvftp dir"))
    filepath=os.path.join("temp", name)
    with open(filepath, "rb") as f:
        ftp.storbinary(f'STOR {name}', f)
    print(f"uploaded successfully")

allfiles=os.listdir("temp")
for f in allfiles:
    t=threading.Thread(target=uploadfile, args=[f])
    threadvar.append(t)
    t.start()
for th in threadvar:
    th.join()
    
shutil.rmtree("temp")
    
# early development comment spree alert frfrffrf!!!11!!