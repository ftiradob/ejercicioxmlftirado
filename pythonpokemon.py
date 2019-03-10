from lxml import etree
doc=etree.parse('pokemonxml.xml')

def listar(doc):
    lista=doc.xpath("/pokedex/pokemon/name/text()")
    return lista

def contartipos(doc):
    tipo=input("Indica el tipo del Pokemon: ")
    listatipo=doc.xpath("/pokedex/pokemon[type='%s']/name/text()"%(tipo))
    print("Hay",len(listatipo),"Pokemon de tipo %s" %(tipo))

def mostrartipo(doc):
    pokemon=input("Indica de qué Pokemon quiere saber el tipo: ").upper()
    print("El/los tipos de este Pokemon es/son: ")
    listanombre=doc.xpath("/pokedex/pokemon[name='%s']/type/text()"%(pokemon))
    return listanombre

def mostraratkpokemon(doc):
    ataque=input("Indica un ataque: ")
    print("Los Pokemon que pueden aprender este ataque son: ")
    print("")
    listaataque=doc.xpath("/pokedex/pokemon/moves/move[name='%s']/../../name/text()"%(ataque))
    return listaataque

def ejer5(doc):
    tipo=input("Indica el tipo del Pokemon: ")
    atk=int(input("Indica el ataque máximo: "))
    print("")
    listapkm=doc.xpath("/pokedex/pokemon[type='%s']/stats[ATK<'%d']/../name/text()"%(tipo,atk))
    return listapkm


print("")
while True:
    print("1. Mostrar el nombre de todos los Pokemon.")
    print("2. Mostrar la cantidad de Pokemon del tipo pedido por teclado.")
    print("3. Pedir un Pokemon por teclado y mostrar de qué tipo es.")
    print("4. Pedir un ataque por teclado y mostrar que Pokemon pueden aprenderlo.")
    print("5. Mostrar los Pokemon de un tipo pedido por teclado y que tengan menos de un determinado ataque pedido por teclado.")
    print("0. Salir")
    opcion=int(input("Elija opción: "))
    
    if opcion==1:
        print("")
        for i in listar(doc):
            print("-",i)
        print("")
    elif opcion==2:
        contartipos(doc)
    elif opcion==3:
        for i in mostrartipo(doc):
            print(i," ",end="")
        print("")
        print("")
    elif opcion==4:
        for i in mostraratkpokemon(doc):
            print("-",i)
        print("")
    elif opcion==5:
        for i in ejer5(doc):
            print("-",i)
        print("")
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")