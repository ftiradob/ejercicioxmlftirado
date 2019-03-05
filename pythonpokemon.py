from lxml import etree
doc=etree.parse('pokemonxml.xml')

def listar(doc):
    lista=doc.xpath("/pokedex/pokemon/name/text()")
    return lista

def contartipos(doc):
    tipo=input("Indica el tipo del pokemon: ")
    listatipo=doc.xpath("/pokedex/pokemon[type='%s']/name/text()"%(tipo))
    print(len(listatipo))


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
        for i in listar(doc):
            print(i)
    elif opcion==2:
        contartipos(doc)
        
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")