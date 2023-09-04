class Fecha: #Se define la clase fecha
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    #Se ajusta el formato   
    def get_fecha(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    def set_fecha(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
    #Tostring    
    def __str__(self):
        return f"Dia: {self.dia}\nMes: {self.mes}\nAño: {self.año}"