# Recall that a stack is a LIFO data structure.

# The method is follows, evaluating the expression from left to right:

#     When you encounter an operand, push it onto the stack
#     When you encounter an operator, pop two values from the stack and push the result back onto the stack
#     When you have finished (been through the whole expression), pop the final answer from the stack

from easyinput import read_line
def RPN(expr):
    stack = []
    
    # A lambda function can take any number of arguments, but can only have one expression.
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y}
    
    nombre_str = str()

    for i in range(len(expr)):
        if expr[i] != ' ' and expr[i] not in ["*", "+", "-"]:
            nombre_str += expr[i]
        if expr[i] == ' ' and len(nombre_str)>0:
            stack.append(int(nombre_str))   
            nombre_str = str()
        
        # El prblema del últim és que he reocrregut tot el vector i no he ficat dintre de la stack perquè la condició per ficar-lo és que el pròxim element sigui un espai en blanc. 
        if i == len(expr)-1 and expr[i] != ' ' and expr[i] not in ["*", "+", "-"]:
            return(nombre_str)

        # Ara el parsing ja està ben fet! Entren els nombres que han d'entrar!
        if expr[i] != ' ' and expr[i] in ["*", "+", "-"]:
            b=stack.pop()       # l'últim que trac és el segon terme de l'operació! El més nou!
            a=stack.pop()
            stack.append((op[expr[i]](a,b)))        # Aquí no puc ficar int, si no 2 -8 em torna 6!
            
    return(stack.pop())       #Últim element


 # Driver Code
if __name__ == "__main__":
     expr = read_line()
     
     while expr is not None:
         # Function call
         print(RPN(expr))
         expr = read_line()

