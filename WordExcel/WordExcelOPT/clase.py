class Persona:
    def __init__(self,nombre,cedula,ciudad,referencia,fecha,inversion):
        self.nombre = nombre
        self.cedula= cedula
        self.ciudad= ciudad
        self.referencia = referencia
        self.fecha= fecha
        self.inversion = inversion
    def __str__(self):
        return(str(self.nombre)+str(self.cedula)+str(self.ciudad)+str(self.referencia)+str(self.fecha)+str(self.sexo))
    def darNombre(self):
        return self.nombre
    def darCedula(self):
        return self.cedula
    def darCiudad(self):
        return self.ciudad
    def darReferencia(self):
        return self.referencia
    def darFecha(self):
        return self.fecha
    def darInversion(self):
        return self.inversion
