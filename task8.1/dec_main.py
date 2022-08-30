from cryptography.fernet import Fernet

with open ('mykey.key','rb') as mykey:
    key = mykey.read()

print(key)

f = Fernet(key)

with open('en_doc.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_doc.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)