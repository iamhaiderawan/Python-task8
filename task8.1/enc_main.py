from cryptography.fernet import Fernet

with open ('mykey.key','rb') as mykey:
    key = mykey.read()

print(key)

f = Fernet(key)

with open('doc.txt', 'rb') as orignal_file:
    orignal = orignal_file.read()

encrypted = f.encrypt(orignal)

with open('en_doc.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
