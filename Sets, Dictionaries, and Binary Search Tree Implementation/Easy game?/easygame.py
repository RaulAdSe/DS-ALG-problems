from easyinput import read
"""
Consider the following game. You start with an empty set of words S. Afterwards, you will be given words one by one. For every given word w, if w is not in S, insert w in S, and if w is already in S, remove w from S. At the end of the process, you must list

    the words that belong to S;
    the words that have been in S, but that finally are not in S.
"""

if __name__ == '__main__':
    has = set()
    had =set()
    game = 1
    quit_s = False
    first = True
    
    inp = read(str)
    while not quit_s:
        while inp != 'END' and inp !='QUIT':
            if inp in has:
                has.remove(inp)
                had.add(inp)
            else:
                has.add(inp)
                if inp in had: # Del segon cas prova pública veiem això
                    had.remove(inp)
            inp = read(str)
    
        if (not first):     
            print() # Blank line
        first = False # Game 1 surt directe, pero entre had de game 1 i títol de game 2 hi ha espai
        
        print("GAME #" + str(game))
        print("HAS:")
        
        list_has = sorted(list(has)) # Sort alphabetically
        for element in list_has:
            print(element)
        print()
        list_had_1 = sorted(list(had)) # First alphabetically
        list_had_2 = sorted(list_had_1, key=len) # Then sort bylength
        print("HAD:")
        for element in list_had_2:
            print(element)
            
        game += 1
        has = set()
        had = set()
        
        if inp =='QUIT':
            quit_s = 1
        else:
            inp = read(str)
        
                
        
# Falta implementar :  The first list must be sorted in alphabetical order. The second list must be sorted by the length of the words (first the shorter words), using alphabetical order to break ties.

