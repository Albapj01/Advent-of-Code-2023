import re

def isAdjacent(line):
    variable = []
    sum, j = 0 , 0
    for i in range(len(line)):
        print(line[i])
        if line[i] == '0' or line[i] == '1' or line[i] == '2' or line[i] == '3' or line[i] == '4' or line[i] == '5' or line[i] == '6' or line[i] == '7' or line[i] == '8' or line[i] == '9':
            if line[i-1] == '+' or line[i-1] == '-' or line[i-1] == '*' or line[i-1] == '/' or line[i-1] == '#' or line[i-1] == '%' or line[i-1] == '^' or line[i-1] == '&':
                if line[i+1] == '.':
                    sum = sum + int(line[i])
            elif line[i+1] == '+' or line[i+1] == '-' or line[i+1] == '*' or line[i+1] == '/' or line[i+1] == '#' or line[i+1] == '%' or line[i+1] == '^' or line[i+1] == '&':
                sum = sum + int(line[i])
            elif line[i+1] == '0' or line[i+1] == '1' or line[i+1] == '2' or line[i+1] == '3' or line[i+1] == '4' or line[i+1] == '5' or line[i+1] == '6' or line[i+1] == '7' or line[i+1] == '8' or line[i+1] == '9':
                if line[i+2] == '+' or line[i+2] == '-' or line[i+2] == '*' or line[i+2] == '/' or line[i+2] == '#' or line[i+2] == '%' or line[i+2] == '^' or line[i+2] == '&':
                    variable[j] = line[i]
                    variable[j+1] =  line[i+1]
                    sum = sum + int(variable)
                elif line[i+2] == '0' or line[i+2] == '1' or line[i+2] == '2' or line[i+2] == '3' or line[i+2] == '4' or line[i+2] == '5' or line[i+2] == '6' or line[i+2] == '7' or line[i+2] == '8' or line[i+2] == '9':
                    if line[i+3] == '+' or line[i+3] == '-' or line[i+3] == '*' or line[i+3] == '/' or line[i+3] == '#' or line[i+3] == '%' or line[i+3] == '^' or line[i+3] == '&':
                        variable[j] = line[i]
                        variable[j+1] =  line[i+1]
                        variable[j+2] =  line[i+2]
                        sum = sum + int(variable)

    print(sum)


f = open("puzzle.txt", "r")

for row in f:
    #separa el fichero cada vez que encuentres un caracter
    line = row.split(' ')
    isAdjacent(line)
    
f.close()