from turtle import title


class Libro(object):
    def __init__(self, id, title, autor, editorial):
        self.id = id
        self.titulo = title
        self.autor = autor
        self.editorial = editorial
    
    def __str__(self):
        return"%s-%s-%s-%s" %\
            (self.id,self.titulo,self.autor,self.editorial)

    def __getattribute__(self, atrib):
        return object.__getattribute__(self,atrib)

class LibroAdmin:
    def __init__(self):
        self.arregLibros = []

    def agregar(self, id, title, autor, editorial):
        lib = Libro(id, title, autor, editorial)
        self.arregLibros.append(lib)
    
    def __str__(self):
        s = ""
        for Libro in self.arregLibros:
            s+= str(Libro) + "\n"
        return s

    def busca(self, clave, por = "id"):
        for indice, Libro in enumerate(self.arregLibros):
            if Libro.__getattribute__(por) == clave:
                return indice

    def remover(self, clave, por = "id"):
        indice = self.buscar(clave)
        if indice!=None:
            self.arregLibros.pop(indice)
            return indice
    
    #Programa principal

    arreglo = LibroAdmin()
    id =input("Id ")
    title =input("Titulo ")
    autor =input("Autor ")
    editorial = input("Editorial ")

    arreglo.agregar(id,title,autor,editorial)
    print("\n", arreglo)

    def remover(self,clave, por="id"):
        indice = self.buscar(clave)
        if indice != None:
            self.arregLibros.pop(indice)
        else:
            return None
    
    #Remover
    elemento

    #Buscar un elemento por ID
    buscando = input("Id del elemento a buscar: ")
    print("Elemento encontrado en posición: {0}".format(arreglo.buscar(buscando)))

    #Remover un elemento por ID
    elemento = input ("Id del elemento a eliminar.")
    print("Elemento a remover de la posición. {0}".format(arreglo.remover(elemento)))

    if i=arreglo.buscar(buscando) != None
        print("Elemento encontrado: {0}".format(i))
    else:
        print("No se encontro elemento")