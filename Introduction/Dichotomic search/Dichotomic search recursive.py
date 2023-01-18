def position(x,v,left,right):     # Since it will be recursive need to specify boundaries which will change
 
    # Check base case
    if right >= left:
 
        mid = (right + left) // 2     # Gives the quotient - the remainder
 
        # If element is present at the middle itself
        if v[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif v[mid] > x:
            return position(x, v, left, mid - 1)
 
        # Else the element can only be present in right subarray
        else:
            return position(x, v, mid + 1, right)
 
    else:
        # Element is not present in the array
        return -1 

# You only need to submit the required procedure; your main program will be ignored.

# Vull la funció en el mateix, nom, paràmetres i ordre de paràmetres que el jutge me demana.
# El jutge correrà la seua funció main fent (arxiu .py que es dona, o també interface) 
# fent servir la meua funció.