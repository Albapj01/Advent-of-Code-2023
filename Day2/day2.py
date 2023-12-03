# Esta función comprueba que se cumplan las condiciones del juego
def isCorrect(game):
    for i in range(len(game)):
        if game[i] == 'red,' or game[i] == 'red;' or game[i] == 'red\n':
            # El valor correspondiente a los cubos rojos es el elemento anterior en la lista 
            if int(game[i-1]) > 12:
                return False
        elif game[i] == 'green,' or game[i] == 'green;' or game[i] == 'green\n':
            if int(game[i-1]) > 13:
                return False
        elif game[i] == 'blue,' or game[i] == 'blue;' or game[i] == 'blue\n':
            if int(game[i-1]) > 14:
                return False
    return True

f = open("puzzle.txt", "r")
total = 0

for row in f:
    # Se separa cada línea en una lista de strings
    game = row.split(' ')

    if isCorrect(game):
        # Como se ha guardado el id junto con :, para poder hacer la suma debemos de omitir el :
        id = game[1].strip(':')
        total = total + int(id)
    
print(total)

f.close()
