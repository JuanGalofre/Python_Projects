import os
from cryptography.fernet import Fernet
files = []
key=None

for file in os.listdir():
    if file == "encryptor.py" or file == "decryptor.py" or file =="thekey.key":
        pass
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key","rb") as keyacceptor:
    key=keyacceptor.read()


for file in files:
    with open(file,"rb") as openedfile:
        content1=openedfile.read()
        decrypted_content = Fernet(key).decrypt(content1)
    with open(file,"wb") as arch:
        arch.write(decrypted_content)
