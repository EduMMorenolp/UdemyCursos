

# 267 - 270

# Ejemplo de herencia Multiple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort()

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Ordenamos el nuevo elemento
        self.ordenar()

# Lista sólo acepta números
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    # Sobreescribimos el método agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar(elemento)

# Lista de Enteros Ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

# Lista enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5,-1, 10, 14, -4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
# Saber las clases padre y su orden
print(ListaEnterosOrdenada.__bases__)
# MRO (Method Resolution Order)
print(ListaEnterosOrdenada.__mro__)

# 268 MRO

class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Método clase1')
class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()
    def metodo(self):
        print('Método clase2')
        super().metodo()
class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()
    def metodo(self):
        print('Método clase3')
        super().metodo()
class Clase4(Clase2, Clase3):

    def metodo(self):
        print('Método clase4')
        super().metodo()

#269

# Creamos objeto clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# mro
print(Clase4.__mro__)
# cual método se ejecuta
clase4.metodo()
