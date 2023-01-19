from easyinput import read

if __name__ == '__main__':
    coup = set()
    alone = set()

    
    inp = read(str)
    while inp is not None:
        if inp == 'affair':
            name_1 = read(str)
            name_2 = read(str)
            
            cerca_1 = [item for item in list(coup) if name_1 in item]   # Cerca primer element
            cerca_2 = [item for item in list(coup) if name_2 in item]   # Cerca segon element
            # Ojo, això hem torna una llista amb un tuple. He de verue si l'element que busco
            # està en la primera o la segona posició
            
            # Vaig a fer tots els casos.
            if cerca_1 == [] and cerca_2 == []:
                coup.add((name_1,name_2)) # Afegeixo tuples de parelles
                if name_1 in alone:  # Com no he trobat intersecció potser està a alone!
                    alone.remove(name_1)
                if name_2 in alone:  # Com no he trobat intersecció potser està a alone!
                    alone.remove(name_2)

            elif cerca_1 != [] and cerca_2 == []:
                if name_2 in alone: # Com no he trobat intersecció potser està a alone!
                    alone.remove(name_2)
                coup.remove(cerca_1[0])
                coup.add((name_1, name_2))
                if cerca_1[0][0] == name_1: # El name_1 estava en primera posició de la parella
                    alone.add(cerca_1[0][1])
                else:
                    alone.add(cerca_1[0][0])
                
                    
                                
            elif cerca_1 == [] and cerca_2 != []:
                if name_1 in alone:  # Com no he trobat intersecció potser està a alone!
                    alone.remove(name_1)
                coup.remove(cerca_1[0])
                coup.add((name_1, name_2))
                if cerca_2[0][0] == name_2: # El name_2 estava en primera posició de la parella
                    alone.add(cerca_2[0][1])
                else:
                    alone.add(cerca_2[0][0])                
           
            elif cerca_1 != [] and cerca_2 != []:   # Al exemple es dona un cas així. Els dos han enganyat a la seua parella
                coup.remove(cerca_1[0])
                coup.remove(cerca_2[0])
                coup.add((name_1, name_2))
                
                if cerca_1[0][0] == name_1: # El name_1 estava en primera posició de la parella
                    alone.add(cerca_1[0][1])
                else:
                    alone.add(cerca_1[0][0])
                
                
                if cerca_2[0][0] == name_2: # El name_2 estava en primera posició de la parella
                    alone.add(cerca_2[0][1])
                else:
                    alone.add(cerca_2[0][0])        
                

                
        elif inp == 'info':
            print('COUPLES:')
            list_coup = (list(coup)) # Ara tinc un problema perquè no puc canviar els tuples! Ho he de convertir
            for i in range(len(list_coup)): # Ordenament alfabètic dintre de les parelles 
                list_coup[i] = list(list_coup[i]) 
                if list_coup[i][0]>list_coup[i][1]:
                   list_coup[i][0], list_coup[i][1] = list_coup[i][1], list_coup[i][0] 
            
            list_coup = sorted(list(list_coup)) # Ordenament alfabètic entre les parelles
                    
            for pair in list_coup: 
                print(str(pair[0]) + ' ' + str(pair[1]))
            print('ALONE:')
            list_alone = sorted(list(alone)) 
            for element in list_alone:
                print(element)
            print('----------')
            
        inp = read(str)