__author__ = 'escabia'

cartas = [["treboles","as"], ["treboles","2"], ["treboles","3"], ["treboles","4"], ["treboles","5"],
          ["treboles","6"], ["treboles","7"], ["treboles","8"], ["treboles","9"], ["treboles","10"],
          ["treboles","sota"], ["treboles","reina"], ["treboles","rey"],["diamantes","as"], ["diamantes","2"],
          ["diamantes","3"], ["diamantes","4"], ["diamantes","5"], ["diamantes","6"], ["diamantes","7"],
          ["diamantes","8"], ["diamantes","9"], ["diamantes","10"], ["diamantes","sota"], ["diamantes","reina"],
          ["diamantes","rey"], ["corazones","as"], ["corazones","2"], ["corazones","3"], ["corazones","4"],
          ["corazones","5"], ["corazones","6"], ["corazones","7"], ["corazones","8"], ["corazones","9"], 
          ["corazones","10"], ["corazones","sota"], ["corazones","reina"], ["corazones","rey"],["picas","as"], 
          ["picas","2"], ["picas","3"], ["picas","4"], ["picas","5"], ["picas","6"], ["picas","7"],
          ["picas","8"], ["picas","9"], ["picas","10"], ["picas","sota"], ["picas","reina"],
          ["picas","rey"]]

mazo_separado = []
for [palo, numero] in cartas:
    if numero == "3":
        mazo_separado.append([palo, numero])

for [palo, numero] in mazo_separado:
    print (numero + " " + palo)
