import os
import requests
import shutil

# IMPORTANT
# Eddit anything in [] before running

print("[PROJECT NAME] Installer")
print("=========================")

#Detects your opporating system, Commet this part out if it is not required
if os.name == "posix":
    pass
else:
    print("[ERROR] You are running Windows or another opperating system which may not be supported")
    print("=========Options=========")
    print("(1) Run Anyway")                                                                             
    print("(Return) Quit")
    
    while True:
        choice = input("Choose a Nomber: ")

        if choice == "1":
            pass
        else:
            quit()

input("Press 'Return' to begin: ")

print("Creating virtual python environment...")
os.system("python -m venv [ENVIRONMANT NAME]")
print("==================")
print("Installing dependencies...")
os.system("source [ENVIRONMANT NAME]/bin/activate && pip install -r requirements.txt")

#================================================
#If you need APT or DNF, Uncomment everything below
#================================================

#print("==================")    
#if shutil.which('apt'):
#    print("APT requirements detected, type sudo password to install")
#    print("Note: You will see what is being installed after typing in your password")
#    os.system("sudo apt install [APT PACKAGES]")
#elif shutil.which('dnf'):
#    print("DNF requirements detected, type sudo password to install")
#    print("Note: You will see what is being installed after typing in your password")           
#    os.system("sudo dnf install [DNF PACKAGES]")
#else:
#    print("Unknown Package Manager, skipping requirements")  

print("==================")
print("Making run.sh executable...")
os.system("chmod +x run.sh")
print("==================")

#================================================
#If you need Folders, Uncomment everything below
#================================================

#print("Making Folders...")
#os.system("mkdir res")                
#os.system("mkdir apk")

print("Done")
quit()

