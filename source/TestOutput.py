import backend
import codecs
'''
file = codecs.open("Files/test.mp3", 'r', encoding="ISO-8859-1")
file2 = codecs.open("Files/test-encrypt.mp3", 'w', encoding="ISO-8859-1")
file3 = codecs.open("Files/test-decrypted.mp3", 'w', encoding="ISO-8859-1")
file4 = codecs.open("Files/test-untouched.mp3", 'w', encoding="ISO-8859-1")
file5 = codecs.open("Files/test-untouched.mp3", "r", encoding="ISO-8859-1")
text = file.read()
obj = backend.ED(string=text, key="saeaahfaihnuyiw23!@#%$626523457:>:KPqxumc8qce.rt93umkurg28724n94yt4877")
file4.write(text)


text2 = file5.read()

obj.ed_mastermethod("encrypt")
file2.write(obj.encrypt_string)
obj.ed_mastermethod("decrypt")
file3.write(obj.decrypt_string)
if text == obj.decrypt_string:
    print("YES")
else:
    print("NO")

if text == text2:
    print("YES!")
else:
    print("NO!")
'''

'''
text = "Johny Johny! Yes Papa? Eating Sugar? No Papa! Telling Lies? No Papa! Open Your Mouth! Ha Ha Ha!"
obj = backend.ED(string=text, key="saea8qce.rt93umkurg28724n94yt4877")

print("Encryption!")
obj.ed_mastermethod(mode="encrypt")
print("\nDecryption!")
obj.ed_mastermethod(mode="decrypt")
'''

