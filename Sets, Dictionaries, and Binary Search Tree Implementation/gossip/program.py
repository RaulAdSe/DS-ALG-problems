from easyinput import read




def write_d(couples): 
      print('COUPLES:')
      s = sorted(couples.items())
      h = len(s)//2
      for i in range(2*h): 
        if s[i][0] < s[i][1]: 
          print(s[i][0], s[i][1])
      

def write_s(alone):        
      print('ALONE:')
      for e in sorted(alone):
        print(e)
      print('-'*10)


def update(p1, p2, couples, alone):
      op1 = couples.get(p1)   
      if op1 is not None: 
          del couples[op1]
          alone.add(op1)                  

      op2 = couples.get(p2)           
      if op2 is not None: 
          del couples[op2]
          alone.add(op2)        
      
      alone.discard(p1)    
      alone.discard(p2)
      couples[p1] = p2
      couples[p2] = p1
      

if __name__ == '__main__':
  couples = dict()
  alone = set()
  ord = read(str)
  while ord is not None:
    if ord == 'info':
      write_d(couples)
      write_s(alone)
    else:
      p1 = read(str) 
      p2 = read(str)
      update(p1,p2,couples,alone)
    ord = read(str)
