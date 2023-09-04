class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
        
    def get_fecha(self):
        return f"{self.dia}/{self.mes}/{self.año}"
    
    def set_fecha(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año
        