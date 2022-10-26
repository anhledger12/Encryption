#Learning about route, solve later
from flask import Flask
chal = Flask(__name__)

@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}

if __name__ == '__main__':
   chal.run()