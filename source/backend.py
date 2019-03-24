# Pycrypt Source Code
import time
import utilityfunc

class ED:

    def __init__(self, string, key):
        self.string = string
        self.key = key
        self.key_c = "0"
        self.next_key_c = "0"
        self.string_c = '0'
        self.encrypt_string = ""
        self.decrypt_string = ""

    def testPrint(self, inp="NULL", out="NULL", key="NULL"):
        print("Input =", inp, "\nOutput =", out, "\nHash Key =", key)

    def dynamic_shift(self):
        if ord(self.next_key_c) % 2 == 1:
            self.string_c = chr((ord(self.string_c) + ord(self.key_c)) % 256)
        else:
            self.string_c = chr((ord(self.string_c) - ord(self.key_c)) % 256)

    def reverse_dynamic_shift(self):
        if ord(self.next_key_c) % 2 == 1:
            self.string_c = chr((ord(self.string_c) - ord(self.key_c)) % 256)
        else:
            self.string_c = chr((ord(self.string_c) + ord(self.key_c)) % 256)

    def caesar_control(self, input_string="Testing", mode="encrypt"):

        #if mode == "encrypt":
            # print("\n\nEncrypting message")
        #elif mode == "decrypt":
            #print("\n\nDecrypting message")
        #else:
            #print("Incorrect mode")
            #exit()
        string_character_index = 0
        key_character_index = 0
        encrypt_string = ""
        decrypt_string = ""
        while string_character_index < len(input_string):  # Oscillating loop

            while key_character_index < len(self.key) and string_character_index < len(input_string):
                # print("Key= ", key_character_index, "String= ", string_character_index)
                # print("Output =", decrypt_string)
                self.key_c = self.key[key_character_index]
                self.string_c = input_string[string_character_index]

                if self.key_c == self.key[-1]:
                    self.next_key_c = self.key[-2]
                else:
                    self.next_key_c = self.key[key_character_index + 1]

                key_character_index += 1
                string_character_index += 1
                if mode == "encrypt":
                    self.dynamic_shift()
                    encrypt_string += self.string_c
                elif mode == "decrypt":
                    self.reverse_dynamic_shift()
                    decrypt_string += self.string_c

            key_character_index -= 1
            # print("Screech")

            while key_character_index >= 0 and string_character_index < len(input_string):
                # print("Key= ", key_character_index, "String= ", string_character_index)
                # print("Output =", self.encrypt_string)
                self.key_c = self.key[key_character_index]
                self.string_c = input_string[string_character_index]

                if self.key_c == self.key[0]:
                    self.next_key_c = self.key[1]
                else:
                    self.next_key_c = self.key[key_character_index - 1]

                key_character_index -= 1
                string_character_index += 1
                if mode == "encrypt":
                    self.dynamic_shift()
                    encrypt_string += self.string_c
                elif mode == "decrypt":
                    self.reverse_dynamic_shift()
                    decrypt_string += self.string_c

        if mode == "encrypt":
            self.encrypt_string = encrypt_string
        elif mode == "decrypt":
            self.decrypt_string = decrypt_string

    def shuffle(self, string, mode = "encrypt"):

        input_string = list(string)
        prime_numbers = utilityfunc.primegen(1630)
        if mode=="encrypt" :
            #print("Shuffling", string[:20])
            string_character_index = 0
            key_character_index = 0
            while string_character_index < len(input_string):  # Oscillating loop

                # print("Key= ", key_character_index, "String= ", string_character_index)
                # print("Output =", decrypt_string)
                if key_character_index == len(self.key):
                    key_character_index = 0
                self.key_c = self.key[key_character_index]
                #print(string_character_index, prime_numbers[ord(self.key_c)], len(input_string), (string_character_index + prime_numbers[ord(self.key_c)]) % len(input_string))
                temp = input_string[string_character_index]
                input_string[string_character_index] = input_string[(string_character_index + prime_numbers[ord(self.key_c)]) % len(input_string)]
                input_string[(string_character_index + prime_numbers[ord(self.key_c)]) % len(input_string)] = temp
                #self.next_key_c = self.key[key_character_index + 1]

                key_character_index += 1
                string_character_index += 1
            #print("KEEEEEEY:", key_character_index-1, '/', len(self.key) - 1)
            self.encrypt_string = ''.join(input_string)



        elif mode=="decrypt":
            #print("Unshuffling", string[:20])
            string_character_index = len(input_string) - 1
            key_character_index = len(input_string) % len(self.key) - 1
            #print("KEEEEEEY:", key_character_index, '/', len(self.key) - 1)

            while string_character_index >= 0:

                # print("Key= ", key_character_index, "String= ", string_character_index)
                # print("Output =", decrypt_string)
                if key_character_index < 0:
                    key_character_index = len(self.key) - 1
                self.key_c = self.key[key_character_index]

               # print(string_character_index, prime_numbers[ord(self.key_c)], len(input_string), (string_character_index + prime_numbers[ord(self.key_c)]) % len(input_string))
                temp = input_string[string_character_index]
                input_string[string_character_index] = input_string[
                    (string_character_index + prime_numbers[ord(self.key_c)]) % len(input_string)]
                input_string[(string_character_index + prime_numbers[ord(self.key_c)]) % len(input_string)] = temp

                self.next_key_c = self.key[key_character_index - 1]

                key_character_index -= 1
                string_character_index -= 1
            self.decrypt_string = ''.join(input_string)

    def ed_mastermethod(self, mode):
        if mode == "encrypt":
            self.caesar_control(self.string, "encrypt")
            i = 0
            while i < 1:
                self.caesar_control(self.encrypt_string, "encrypt")
                i += 1
                print("Cycle No:", i)

            #self.shuffle(self.encrypt_string, mode="encrypt")

            self.testPrint(self.string, self.encrypt_string, self.key)
        if mode == "decrypt":
            i = 0
            #self.shuffle(self.encrypt_string, mode="decrypt")

            self.caesar_control(self.encrypt_string, "decrypt")
            while i < 1:
                i += 1
                self.caesar_control(self.decrypt_string, "decrypt")

                print("Cycle No:", i)

            self.testPrint(self.encrypt_string, self.decrypt_string, self.key)

