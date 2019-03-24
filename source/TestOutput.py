import backend
import codecs

file = codecs.open("test.png", 'r', encoding="ISO-8859-1")
file2 = codecs.open("test2.png", 'w', encoding="ISO-8859-1")
file3 = codecs.open("test3.png", 'w', encoding="ISO-8859-1")
file4 = codecs.open("test4.png", 'w', encoding="ISO-8859-1")
text = file.read()
obj = backend.ED(string=text, key="saeaahfaihnuyiw23!@#%$626523457:>:KPqxumc8qce.rt93umkurg28724n94yt4877")
file4.write(text)

file5 = codecs.open("test4.png", "r", encoding="ISO-8859-1")
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


