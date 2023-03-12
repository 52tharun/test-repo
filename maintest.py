

def quotient_remainder(a,b):
    if b == 0:
        raise ValueError('B must be positive')
    
    myTuple = divmod(a,b)

    if myTuple[1] < 0:
        newTuple1 = myTuple[0] + 1
        newTuple2 = myTuple[1] - b

        newTuple = (newTuple1, newTuple2)
        return newTuple

    return myTuple



assert quotient_remainder(7, 3) == (2, 1)


# Check that the function raises a ValueError for b = 0
try:
    quotient_remainder(7, 0)
except ValueError:
    print("ValueError was raised as expected")
else:
    print("Error: function should have raised a ValueError")

print("All tests passed!")

