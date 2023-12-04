total = 0
maxs = 0

# Esta función calcula el máximo de los valores de los cubos rojos, verdes y azules y los múltiplica
def maximum(game):
    x,y,z = [], [], []
    max_red, max_green, max_blue, totalMax = 0, 0, 0, 0

    for i in range(len(game)):
        if game[i] == 'red,' or game[i] == 'red;' or game[i] == 'red\n':
            # El valor correspondiente a los cubos rojos es el elemento anterior en la lista 
            x.append(int(game[i-1]))
            # Calculamos el máximo de los valores de los cubos rojos
            max_red = max(x)
        elif game[i] == 'green,' or game[i] == 'green;' or game[i] == 'green\n':
            y.append(int(game[i-1]))
            max_green = max(y)
        elif game[i] == 'blue,' or game[i] == 'blue;' or game[i] == 'blue\n':
            z.append(int(game[i-1])) 
            max_blue = max(z)
            
    totalMax = max_red * max_green * max_blue

    return totalMax


f = open("puzzle.txt", "r")

for row in f:
    # Se separa cada línea en una lista de strings
    game = row.split(' ')
    maxs = maximum(game)
    total = total + maxs

print(total)    

f.close()