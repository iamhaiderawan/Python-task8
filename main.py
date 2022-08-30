from cryptography.fernet import Fernet

key =Fernet.generate_key()

command = Fernet(key)

pw = command.encrypt(b'mypassword')
decryptstr = command.decrypt(pw)

print('Key: ', (str(key, 'utf8')))
print('our encrypted text: ', (str(pw, 'utf8')))
print('our decrypted text: ', (str(decryptstr, 'utf8')))