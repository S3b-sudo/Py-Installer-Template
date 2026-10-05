import os
import requests

# IMPORTANT
# Eddit anything in [] before running

print("[NAME OF PROJECT] Installer")
print("==================")
input("Press 'Return' to begin: ")
print("Creating virtual python environment...")
os.system("python -m venv [ENVIRONMENT NAME]")
print("==================")
print("Installing dependencies...")
os.system("source [ENVIRONMENT NAME]/bin/activate && pip install -r requirements.txt")
print("==================")
print("Making run.sh executable...")
os.system("chmod +x run.sh")
print("==================")

#print("Making Folders...")
#os.system("mkdir res")
#os.system("mkdir apk")

print("Done")
quit()
