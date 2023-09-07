import csv
class Registro:
    global se_puede_agregar
    
    def __init__(self, Usuarios, numRegistros):
        self.Usuarios = Usuarios
        self.numRegistros = numRegistros
        
    def se_puede_agregar(self):
        if len([x for x in self.Usuarios if x!= None and x not in self.Usuarios]) +1 < self.numRegistros:
            return True
        else:
            return False
          
    def agregar(self, usuario):
        if se_puede_agregar(self):
            for i in range(len(self.Usuarios)):
                if self.Usuarios[i] == None:
                    self.Usuarios[i] = usuario
                    break
            self.sortear()
                          
    def sortear(self):
        for i in range(1, self.numRegistros):
            
            
            j = i-1
            if self.Usuarios[j] != None and self.Usuarios[j+1] != None:
                
                key = self.Usuarios[i]
                while (j>=0 and self.Usuarios[j].get_id() > key.get_id()):
                    self.Usuarios[j+1] = self.Usuarios[j]
                    j-= 1
                self.Usuarios[j+1] = key
            elif self.Usuarios[j] == None and self.Usuarios[j+1] != None:
                self.Usuarios[j] = self.Usuarios[j+1]
                self.Usuarios[j+1] = None
                
        
            
    def eliminar(self, id):
        for i in range(len(self.Usuarios)):
            if self.Usuarios[i] != None and self.Usuarios[i].get_id() == id:
                #print(self.Usuarios[i])
                self.Usuarios[i] = None 
                self.sortear()
                break
    
    def buscar(self, id):
        for x in self.Usuarios:
            if x!= None and x.get_id() == id:
                return x
    def get_usuarios(self):
        return self.Usuarios
            
    def __str__(self):
        r = ""
        for x in self.Usuarios:
            if x != None:
                r += str(x) + "\n"
        return r