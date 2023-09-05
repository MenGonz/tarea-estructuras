from Registro import Registro
from Usuario import Usuario
import csv 


numregistro = 8
registro = Registro([None]*numregistro,numregistro)

with open("datos.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        usuario = Usuario(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        registro.agregar(usuario)
        

if input("¿Desea añadir un nuevo registro? (si/no)") == "si":
    nombre = input("Ingrese el nombre del usuario: ")
    id = input("Ingrese el id del usuario: ")
    fecha_nac = input("Ingrese la fecha de nacimiento del usuario: ")
    ciudad_nac = input("Ingrese la ciudad de nacimiento del usuario: ")
    dir = input("Ingrese la dirección del usuario: ")
    tel = input("Ingrese el teléfono del usuario: ")
    email = input("Ingrese el email del usuario: ")
    registro.agregar(Usuario(id,nombre,fecha_nac,ciudad_nac,dir,tel,email))
    
if input("¿Desea eliminar un registro? (si/no)") == "si":
    id = input("Ingrese el id del usuario a eliminar: ")
    registro.eliminar(id)
    
if input("¿Desea buscar un registro? (si/no)") == "si":
    id = input("Ingrese el id del usuario a buscar: ")
    print(registro.buscar(id))
