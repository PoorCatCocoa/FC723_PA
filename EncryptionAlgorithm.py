class EncryptionAlgorithm:
    def __init__(self):
        self.key: int = 0

    def get_key(self):      #get the encryption key from user
        self.key = int(input("Please enter the encryption key: \n"))
        if not self.prime_check():
            print("!!! The encryption key must be a prime number !!!\n")
            exit()

    def e_gcd(self, a: int, b: int) -> int:     #find the gcd
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def prime_check(self) -> bool:      #check the key to make sure it's prime
        if self.e_gcd(self.key, 256) != 1:
            print(self.key, self.e_gcd(self.key, 256))      # use 256 to make sure the key won't get more the maximum number of ASCII
            return False
        return True

    def encrypt(self, origin_text: str) -> str:     #encrypt the text using ceaser-cipher
        if self.key == 0:       # get the key every time before encryption
            self.get_key()
        ciphertext = ""
        for char in origin_text:
            cipherchar = chr((ord(char) + self.key) % 256)
            ciphertext += cipherchar
        self.key = 0        #clean the key every time used
        return ciphertext

    def decrypt(self, cipher_text: str) -> str:     #decrypt the text using ceaser-cipher
        if self.key == 0:       # get the key every time before decryption
            self.get_key()
        encodetext = ""
        for char in cipher_text:
            encodechar = chr((ord(char) - self.key) % 256)
            encodetext += encodechar
        self.key = 0        #clean the key every time used
        return encodetext

    def e_exit(self):       #exit the program
        exit()

    def e_main(self):
        while True:
            mode: int = int(input("You are using the EncryptionAlgorithm\n"
                    "Choose the mode you want to use: \n"
                    "1. Encrypt \n"
                    "2. Decrypt \n"
                    "3. Exit \n"
                ))
            match mode:
                case 1:
                    origin_text = input("Please enter the text you want to encrypt: \n")
                    print("The encrypted text is: \n", self.encrypt(origin_text))
                case 2:
                    cipher_text = input("Please enter the text you want to decrypt: \n")
                    print("The decrypted text is: \n", self.decrypt(cipher_text))
                case 3:
                    print("Bye~")
                    self.e_exit()

main = EncryptionAlgorithm()        #initialize
main.e_main()       #run the program