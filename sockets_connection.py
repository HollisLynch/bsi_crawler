import sys
import socket
import scrapy
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
"""
A network socket is an endpoint of an interprocess communication across a computer network. 
The Python Standard Library has a module called socket which provides a low-level internet networking interface.
"""
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % err)

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("Connected to google")


def rsa(message):
    """
    Generating new keys
        Generating a keypair may take a long time, depending on the number of bits required. 
        The number of bits determines the cryptographic strength of the key, as well as the size of the message you can encrypt.
    """
    key = RSA.generate(2048)
    private_key = key.exportKey('PEM')
    public_key = key.publickey().exportKey('PEM')
    """ Encrypting message using public key """
    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    encrypted_text_b64 = base64.b64encode(encrypted_text)
    print('encrypted message: {}'.format(encrypted_text_b64))
    """ Decrypting message using private key """
    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)
    print('decrypted message: {}'.format(decrypted_text))


message = input('Enter the message: ')
message = str.encode(message)
rsa(message)

s.send(message)
data = s.recv(1024)

s.close()
