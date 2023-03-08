

def quotient_remainder(a,b):
    if b == 0:
        raise ValueError ('B must be positive')
        exit()
    
    myTuple = divmod(a,b)

    if myTuple[1] < 0:
      newTuple1 = myTuple[0] + 1
      newTuple2 = myTuple[1] - b

      newTuple = (newTuple1, newTuple2)
      return newTuple
  
    return myTuple


printvalue = quotient_remainder (-10,-3)

print (printvalue)
print"commit1 test"

