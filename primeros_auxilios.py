import sys

print("Programa de primeros Auxilios")

estimulos = str(input("¿Responde a Estimulos? Escriba si o no = "))
ambulancia="no"

if estimulos == "si": 
    print("Debe llevarlo al hospital más cercano \n ")
    print("Programa Finalizado")
    sys.exit()
elif estimulos == "no":
    print("Abrir la vía Aérea \n")
    respira = input("¿Respira? Escriba si o no = ")
    if respira == "si":
        print("Permitirle posición de suficiente ventilación \n")
        sys.exit()
    elif respira == "no":
        print("Administrar 5 ventilaciones y llamar a Ambulancia \n")
        
        ambulancia = "no"  # Inicializar la variable ambulancia
        while ambulancia == "no":
            signos = input("¿Tiene Signos de vida? Escriba si o no = ")
            if signos == "no":
                print("Administrar Revaluar a la espera de la ambulancia \n")
            elif signos == "si":
                print("Reevaluar a la espera de la ambulancia \n")
                
            ambulancia = input("¿Llegó la ambulancia? Escriba si o no = ")

        print("Ha llegado la ambulancia - Programa finalizado")
        
         
     