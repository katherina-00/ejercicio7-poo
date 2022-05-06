class ViajeroFrecuente:
    __numViajero=0
    __dni=0
    __nombre=""
    __apellido=""
    __millas_acum: int=0

    def __init__(self,numViajero,dni,nombre,apellido,millas_acum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def __str__(self):
        return "%d %d %s %s %d" % (self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
    def getMillas(self):
        return self.__millas_acum
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def setMillas(self,nuevasMillas):
        self.__millas_acum=nuevasMillas

    def __eq__(self, other):
        if type(self) == type(other):
            return other.getMillas() == self.__millas_acum
        else:
            if type(other)==int or type(other)==float:
                return self.__millas_acum == other
        return other == self.__millas_acum

    def __add__(self, other):
        retorno=None
        if type(other)== int:
            self.__millas_acum + other
            retorno = self
        if type(other)==ViajeroFrecuente:
            self.__millas_acum + other.getMillas()
            retorno = self
        return retorno
    def __sub__(self, other):
        retorno=None
        if type(other)== int:
            self.__millas_acum - other
            retorno = self
        if type(other)==ViajeroFrecuente:
            self.__millas_acum - other.getMillas()
            retorno = self
        return retorno

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__sub__(other)
