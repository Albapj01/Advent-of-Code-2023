import re

def convert_to_numbers(row):
    """ Para que reemplace todas las palabras por sus correspondientes números y letras iniciales o finales, 
        según puedan causar que no se identifique otro número. Por ejemplo: zerone se remplazaría por 0ne y 
        necesitamos que se reemplace por 0one para obtener 01 """
    x = row.replace('zero', '0o')
    x = x.replace('one', 'o1e')
    x = x.replace('two', 't2o')
    x = x.replace('three', 't3e')
    x = x.replace('four', '4')
    x = x.replace('five', '5e')
    x = x.replace('six', '6')
    x = x.replace('seven', '7n')
    x = x.replace('eight', 'e8t')
    return x.replace('nine', 'n9e')

 
 # Abrir fichero en modo lectura
f = open("puzzle.txt", "r")
sumTotal=0

for row in f:
    
    # Guarda la primera ocurrencia de un número
    variable = re.search('[0-9]', convert_to_numbers(row)) 
    variable = int(variable.group(0))
        
    # Invierte la cadena 
    x = convert_to_numbers(row)
    x = x[::-1]
    
    # Guarda la primera ocurrencia de un número en la cadena invertida
    variable2 = re.search('[0-9]', convert_to_numbers(x))
    variable2 = int(variable2.group(0))

    sumRow = str(variable) + str(variable2)
    sumTotal = sumTotal + int(sumRow)
  
print(sumTotal)

f.close()