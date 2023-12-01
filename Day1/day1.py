import re

# Abrir fichero en modo lectura
f = open("puzzle.txt", "r")
sumTotal=0

for row in f:
    # Guarda la primera ocurrencia de un número
    variable = re.search('[0-9]', row) 
    variable = int(variable.group(0))
    
    # Invierte la cadena 
    row = row[::-1] 

    # Guarda la primera ocurrencia de un número en la cadena invertida
    variable2 = re.search('[0-9]', row)
    variable2 = int(variable2.group(0))

    sumRow = str(variable) + str(variable2)
    sumTotal = sumTotal + int(sumRow)
  
print(sumTotal)

