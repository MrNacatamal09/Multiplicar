'''
Autor: Adolfo C. Ramirez A.
Fecha: 16/05/25
Versión: 1.0
Descripción: 
Escriba un programa que calcule la tabla de multiplicar del número n
Desde el 1 hasta m
'''

import os

def multiplicar():
    print("******** TABLA DE MULTIPLICACIÓN ********")
    n=int(input("Digite el multiplicando máximo de la tabla: "))
    m=int(input("Digite el multiplicador: "))
    os.system("cls")
    print("-----------------------------------------------------")
    print(f"//////// TABALA DE MULTIPLICAR del 1 hasta {n} ////////")
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(f"{i} x {j} = {i*j}")    
        print("\n")
    print("-------------------------------------------------------")
    

multiplicar()