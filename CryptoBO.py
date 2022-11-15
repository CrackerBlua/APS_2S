from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

# Definimos o Block Size para 16
BS = 16

# Lambda functions que faz o processo de pad/unpad de acordo com o tamanho do texto a ser inserido e o Block Size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

# Classe que fará todo o processo de criptografar e decriptografar
class AESCipher:
    
    # Construtor da classe
    def __init__(self):
        self.key = ''
        self.message = ''
        self.block_size = AES.block_size

    # Função que fornecerá uma chave aleatória de 16bytes
    def set_random_key(self):
        self.key = get_random_bytes(16)
    
    # Função que servirá para colocar uma chave manualmente
    def set_custom_key(self, key):
        self.key = key
    
    # Função que fará todo o processo de criptografia
    def encrypt(self, plain_text):
        # Fazemos a mensagem passar pelo processo de pad
        plain_text = pad(plain_text)
        # Gerá um IV que é um requisito para essa criptografia
        iv = Random.new().read(self.block_size)
        # Geramos a cifra
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Geramos o texto encriptografado 
        encrypted_text = cipher.encrypt(plain_text.encode())
        # Definimos nossa mensagem e codificamos em base64
        self.message = b64encode(iv + encrypted_text).decode("utf-8")
    
    # Função que fará todo o processo de descriptografia
    def decrypt(self):
        # Decodificamos a mensagem que estava em base64
        self.message = b64decode(self.message)
        # Geramos nosso IV
        iv = self.message[:self.block_size]
        # Geramos a cifra
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # Retornamos a mensagem descriptografada
        self.message = cipher.decrypt(self.message[self.block_size:]).decode("utf-8")