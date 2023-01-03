import subprocess
import os
import time
# print(os.system("nslookup apple.com"))

domain = "summer.com"
command = "nslookup {}".format(domain)
command_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)



print(command_output)
if 'Non-existent domain' in str(command_output):
    print("Domain {} does not exist".format(domain))
else:
    print("Domain {} exists".format(domain))
