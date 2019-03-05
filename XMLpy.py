from lxml import etree
doc=etree.parse('xml_pokemon')

def listar(doc):
    lista=doc.xpath("/pokedex/pokemon/name/text()")
    return lista

def contar(doc):
    cuenta=doc.xpath("count(/pokedex/pokemon/name/text())")
    return cuenta


print("")
while True:
    print("1. Mostrar el nombre de todos los Pokemon.")
    print("2. Mostrar la cantidad de Pokemon que tienen más vida que la indicada por teclado.")
    print("3. Pedir un Pokemon por teclado y mostrar de qué tipo es.")
    print("4. Pedir un ataque por teclado y mostrar que Pokemon pueden aprenderlo.")
    print("5. Mostrar los Pokemon de un tipo pedido por teclado y que tengan menos de un determinado ataque pedido por teclado.")
    print("0. Salir")
    opcion=int(input("Elija opción: "))
    
    if opcion==1:
        print(listar)
    elif opcion==2:
        print(" Hay ", int(contar(doc))," Pokemon que tienen más vida que la indicada por teclado.")
        
    elif opcion==0:
        print("Adios")
        break
    else:
        print("Error de opción")