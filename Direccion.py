class Direccion():
    
    def __init__(self,calle, noCalle, nomenclatura, barrio,ciudad):
        self.calle = calle
        self.noCalle = noCalle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
         
    #Getters
    def get_calle(self):
        return self.calle
    def get_noCalle(self):
        return self.noCalle
    def get_nomenclatura(self):
        return self.nomenclatura
    def get_barrio(self):
        return self.barrio
    def get_ciudad(self):
        return self.ciudad
        
    def __str__(self):
        return f"""{self.get_calle} {self.get_noCalle}  #{self.get_nomenclatura} Barrio {self.get_barrio}, Ciudad {self.get_ciudad} """