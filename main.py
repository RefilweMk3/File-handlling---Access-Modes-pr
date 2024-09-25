file=open("student portal.txt","r")
print(file.read())
file.close()

file=open("Emily.txt","w")
file.write("Hello Emily welcome to ur Student portal I am Mr Johnson and I will be ur teacher for today...")
file.close()

file=open("Brain.txt","a")
file.write("\n Heres a new python portal")
file.close()



f1=open("Musa.txt","a+")
f2=open("Siya.txt","r")
f1.write(f2.read())
f1.seek(0)
f2.seek(0)
print(f1.read())
print(f2.read())
