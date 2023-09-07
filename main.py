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
        
res = input("¿Desea añadir un nuevo registro? (si/no)")
if res == "si":
    nombre = input("Ingrese el nombre del usuario: ")
    id = input("Ingrese el id del usuario: ")
    fecha_nac = input("Ingrese la fecha de nacimiento del usuario: ")
    ciudad_nac = input("Ingrese la ciudad de nacimiento del usuario: ")
    dir = input("Ingrese la dirección del usuario: ")
    tel = input("Ingrese el teléfono del usuario: ")
    email = input("Ingrese el email del usuario: ")
    registro.agregar(Usuario(id,nombre,fecha_nac,ciudad_nac,dir,tel,email))
    
res = input("¿Desea eliminar un registro? (si/no)")
if res == "si":
    id = input("Ingrese el id del usuario a eliminar: ")
    registro.eliminar(id)
    
res= input("¿Desea buscar un registro? (si/no)")
if res == "si":
    id = input("Ingrese el id del usuario a buscar: ")
    print(registro.buscar(id))
    
for i in range(len(registro.get_usuarios())):
    if registro.get_usuarios()[i] != None:
        vec = [registro.get_usuarios()[i].get_id(),registro.get_usuarios()[i].get_nombre(),registro.get_usuarios()[i].get_fecha_nac(),registro.get_usuarios()[i].get_ciudad_nac(),registro.get_usuarios()[i].get_dir(),registro.get_usuarios()[i].get_tel(),registro.get_usuarios()[i].get_email()]
        if i == 0:
            with open('datos.csv', 'w', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(vec)
        else:
            with open('datos.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(vec)
    

#print(registro)
