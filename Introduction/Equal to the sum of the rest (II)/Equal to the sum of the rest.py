# -*- coding: utf-8 -*-
#Created on Fri Oct 14 20:19:17 2022
#@author: raulc


from easyinput import read

# =============================================================================
# Write a program that, given a sequence of integer numbers, tells if there is any number equal to the sum of the rest.
# =============================================================================

def suma_demas(v,s):
    for i in range(len(v)):
        if v[i] == s - v[i]: return True
    return False

if __name__ == '__main__':
    n = read(int)
    while n is not None:
        v = [0]*n
        sum = 0
        for j in range(n):
            v[j] = read(int)
            sum += v[j]
        if suma_demas(v, sum): print('YES')
        else: print('NO')
        n = read(int)
        
# 4   3 4 -1 2
# 7   1 0 3 3 1 0 2
# 1   0
# 1   -4
# 2   -3 -3
# 3   -1 -4 -5
#Copy the input, then execute and paste my input.

#Caldrà ordenar mitjançant els algorismes per a fer els exercicis.
# python3 sum_of_the_rest.py < input (el input debe estar en la misma carpeta que el archivo!)

#Per a que funcione s'ha d'obrir una nova consola continuament.

        