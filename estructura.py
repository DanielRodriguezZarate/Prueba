#conjuntos
c = set()
c.add(10)
c.add(5)
c.add(15)
c.add("Hola")
c.add("Zorro")
print(c)

#Copia
c2 = c.copy()
print(c2)
c2.add(100)
print(c2)

#Direferencia de conjuntos
print(c.difference(c2))
print(c2.difference(c))

#Intersección
print(c.intersection(c2))

#otro
print(c.issuperset(c2))
print(c2.issuperset(c))