import re

class Cipher:
    cipher=str
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self, cipher_keyword:str):
        self.cipher=cipher_keyword.upper()
        for i in self.abc:
            if i not in cipher_keyword.upper():
                self.cipher=self.cipher+i
        print(self.cipher)
    
    def encode(self, encode_string:str):
        encoded=""
        for i in encode_string.upper():
            if i == " ":
                encoded+=" "
            else:
                encoded+=self.cipher[self.abc.find(i)]
        print(encoded)

    def decode(self,decode_string:str):
        decoded=""
        for i in decode_string.upper():
            if i == " ":
                decoded+=" "
            else:
                decoded+=self.abc[self.cipher.find(i)]
        print(decoded)

cipher = Cipher("crypto")
cipher.encode("Hello world")
cipher.decode("Fjedhc dn atidsn")