# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:53:08 2022

@author: raulc
"""

def insertion_sort(v):
 
    # Traverse through 1 to len(arr), faig l'anàlisi sense considerar el 0 perquè precisament buscaré el candidat per aqueta posició.
    # Si aquesta posició ja està ben ficada, perfecte.
    for i in range(1, len(v)):
 
        key = v[i]
        
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        
        # Sempre moc els que tenen una indexació inferior!
        # Amb això aconseguieixo que de la key cap a l'esquerra sempre estiguen ordenats.
        
        j = i-1
        while j >=0 and key < v[j] :
                v[j+1] = v[j]
                j -= 1
        v[j+1] = key
        
        # volem que de return tingui None, ergo no li fico return