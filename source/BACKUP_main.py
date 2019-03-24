# Pycrypt Source Code
import time

start_time = time.time()






def primegen(num_range):
    width = num_range

    print("Width=", width)
    counter = 0
    num_list = []
    for i in range (3, width+1, 2):
        num_list.append(i)

    for prime in num_list:
        print(counter, ")", prime)
        counter+=1
        for multiplyer in num_list[num_list.index(prime):]:
            #print( multiplyer, '*', prime)
            try:
                num_list.remove(prime*multiplyer)
            except:
                if prime*multiplyer > width:
                    break
                print("Redundant!!!!!!!!!!!!!!!!!!!!!!1", multiplyer, " ", prime)
    num_list.insert(0, 2)
    return num_list
    print("--- %s seconds ---" % (time.time() - start_time))



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

        if mode == "encrypt":
            print("\n\nEncrypting message")
        elif mode == "decrypt":
            print("\n\nDecrypting message")
        else:
            print("Incorrect mode")
            exit()
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
        print("SHUFLiNG!!!!!!!!!!!!!!!!!!!")
        input_string = list(string)
        prime_numbers = primegen(1630)
        if(mode=="encrypt"):
            string_character_index = 0
            key_character_index = 0
            while string_character_index+1 < len(input_string):  # Oscillating loop

                # print("Key= ", key_character_index, "String= ", string_character_index)
                # print("Output =", decrypt_string)
                if key_character_index >= len(self.key):
                    key_character_index = 0
                self.key_c = self.key[key_character_index]
                self.string_c = input_string[string_character_index]

                #self.next_key_c = self.key[key_character_index + 1]

                key_character_index += 1
                string_character_index += 1



        if(mode=="decrypt"):
            string_character_index = len(input_string)
            key_character_index = len(self.key)

            while string_character_index-1 > 0:

                # print("Key= ", key_character_index, "String= ", string_character_index)
                # print("Output =", decrypt_string)
                if key_character_index < 0:
                    key_character_index = len(self.key)
                self.key_c = self.key[key_character_index]
                self.string_c = input_string[string_character_index]

                self.next_key_c = self.key[key_character_index - 1]

                key_character_index -= 1
                string_character_index -= 1

                temp = input_string[string_character_index]
                input_string[string_character_index] = input_string[string_character_index + prime_numbers[ord(self.key_c)] ]
                input_string[string_character_index + prime_numbers[ord(self.key_c)] ] = temp












# Testing Inputs

obj = ED("It was Ms. Fitzhugh. She was walking fast. A strange expression crossed the faces of the students as they glanced"
         " toward the door and saw the principal go straight into the boys’ restroom. The footsteps stopped. There was a deep,"
         "throaty sound difficult to describe. Then came an eruption of shrill screaming and a rapid sound of heels."
         "Moments later, Ms. Fitzhugh emerged, her eyes wild. Screaming, she skidded in the hall and headed toward the office.", "Awqe234zf90kr#")
obj.caesar_control(obj.string, "encrypt")
obj.testPrint(obj.string, obj.encrypt_string, obj.key)
obj.caesar_control(obj.encrypt_string, "decrypt")
obj.testPrint(obj.encrypt_string, obj.decrypt_string, obj.key)
obj.shuffle(obj.string)
obj.testPrint(obj.string, obj.encrypt_string)

'''
x = 'A'
print(x)

print("1 =", chr(49))

x = chr(ord(x)+1)
print(x)
'''
