from cryptography.fernet import Fernet

# key = Fernet.generate_key()

# with open('mykey.key', 'wb') as mykey:
#     mykey.write(key)

with open ('mykey.key','rb') as mykey:
    key = mykey.read()

print(key)

# f = Fernet(key)

# with open('doc.txt', 'rb') as orignal_file:
#     orignal = orignal_file.read()

# encrypted = f.encrypt(orignal)

# with open('en_doc.txt', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted)

# f = Fernet(key)

# with open('en_doc.txt', 'rb') as encrypted_file:
#     encrypted = encrypted_file.read()

# decrypted = f.decrypt(encrypted)

# with open('dec_doc.txt', 'wb') as decrypted_file:
#     decrypted_file.write(decrypted)