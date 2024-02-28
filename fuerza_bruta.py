import getpass
from string import ascii_lowercase

intentos=0
password = getpass.getpass("Ingrese su clave secreta: ")

for i in range(len(password)):
    for j in range(len(ascii_lowercase)):
        intentos += 1
        if password[i] == ascii_lowercase[j]:
            break
    
print(f'La Contraseña fue forzada en {intentos} intentos')
