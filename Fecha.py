class Fecha: #Se define la clase fecha
    def __init__(self, fecha):
        self.fecha = fecha
    #Se ajusta el formato   
    def get_fecha(self):
        return f"{self.fecha}"
    
    def set_fecha(self, fecha):
        self.fecha = fecha
    #Tostring    
    def __str__(self):
        return f"Fecha: {self.get_fecha()}"