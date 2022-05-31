


cod = int(input("digite el codigo del estuadiante: "))
nombre = input("digite el nombre del estuadiante: ")


if cod!=0:
    nota1=float(input("digite la nota del parcial 1: "))
    nota2=float(input("digite la nota del parcial 2: "))
    nota3=float(input("digite la nota del parcial 3: "))
else:
    print ("fin de los datos de entrada: ")

reprobados = 0

while cod !=0:
    nota_final = (nota1 + nota2 + nota3)/3
    print ("el resultado del codigo "+ str (cod) + ", cuyo nombres " + nombre + ",obtuvo una nota definitiva de " + str (nota_final))

    if nota_final < 3:
        reprobados = reprobados + 1
        cod= int(input("digite el codigo del estudiante: "))
        nombre = input("digite el nombe del estuadiante: ")

    if cod !=0:
        nota1 = float(input("digite la nota del parcial 1: "))
        nota2 = float(input("digite la nota del parcila 2: "))
        nota3 = float(input("digitel a nota del parcial 3: "))
    
    else:
        print("fin de los datos de entrada. ")

    print("cantidad de estudiantes que  reprobaron la materia: " + str(reprobados))
