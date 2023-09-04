import csv
class Registro:
    def __init__(self, Usuarios, numRegistros):
        self. Usuarios = Usuarios
        self.numRegistros = numRegistros
        
    def se_puede_agregar(self, usuario):
        if len([x for x in self.Usuarios if x!= None and x not in self.Usuarios]) +1 < self.numRegistros:
            return True
        else:
            return False
          
    def agregar(self, usuario):
        if se_puede_agregar(usuario):
            for i in range(len(self.Usuarios)):
                if self.Usuarios[i] == None:
                    self.Usuarios[i] = usuario
                    break
            self.sortear()
                          
    def sortear(self):
        for i in range(1, self.numRegistros):
            j=1
            
            while (j>0 and (self.Usuarios[j-1].get_id() > self.Usuarios[j].get_id() or self.Usuarios[j-1] == None)  ):
                self.Usuarios[j], self.Usuarios[j-1] = self.Usuarios[j-1], self.Usuarios[j]
                j-= 1
                
        
            
    def eliminar(self, id):
        for x in self.Usuarios:
            if x != None and x.get_id() == id:
                x = None 
                self.sortear()
    
    def buscar(self, id):
        for x in self.Usuarios:
            if x!= None and x.get_id() == id:
                return x