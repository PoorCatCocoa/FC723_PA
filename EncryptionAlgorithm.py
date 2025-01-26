class EncryptionAlgorithm:
    def __init__(self, key: int):
        self.key = key
        # if not self.prime_check():
        #     print("!!! The encryption key must be a prime number !!!\n")
        #     exit()

    def e_gcd(self, a: int, b: int) -> int:
        if a and b != 0:
            while b != 0:
                r = a % b
                a = b
                b = r
                return a

    def prime_check(self) -> bool:
        if self.e_gcd(self.key, 256) != 1:
            print(self.key, self.e_gcd(self.key, 256))
            return False
        return True

    def encrypt(self, origin_text: str) -> str:
        ciphertext = ""
        for char in origin_text:
            cipherchar = chr((ord(char) + self.key) % 256)
            ciphertext += cipherchar
        return ciphertext

    def decrypt(self, cipher_text: str) -> str:
        encodetext = ""
        for char in cipher_text:
            encodechar = chr((ord(char) - self.key) % 256)
            encodetext += encodechar
        return encodetext




#c = EncryptionAlgorithm(int(input("Please enter the encryption key: \n")))
c= EncryptionAlgorithm(1).e_gcd(3, 256)
print(c)