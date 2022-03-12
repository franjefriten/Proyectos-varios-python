

# os.makedirs(name=r"C:\Users\kikof\Desktop\Directory_Proviing")
# os.chdir(path=r"C:\Users\kikof\Desktop\Directory_Proviing")
# with open(r"C:\Users\kikof\Desktop\Directory_Proviing\Text.txt", "w") as file:
#    Lines = [str(input("Línea {0}".format(i))) for i in range(0, 5) ]
#    file.writelines(Lines)
# file.close()

l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v for s in m
           for v in l
           if v > 0]

def contador(max):
    print("=Dentro de contador - empezando")
    n=0
    while n < max:
        print(f"=Dentro de contador - viene yield con n={n}")
        yield n
        print("=Dentro de contador - retomando después de yield")
        n=n+1
    print("=Dentro de contador - terminando")

print("Instanciando contador") 
mycont = contador(3)
print("Contador instanciado") 

for i in mycont:
    print(f"valor leido del iterador={i}") 
print("Listo") 

