class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone

    # método get (utilizando property)
    @property
    def nome(self):
        return self._nome
    
    # método set (utilizando setter)
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
