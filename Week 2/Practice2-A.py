M = [ ]
def print_prime_numbers (n) :
    
    for r in range(2 , ((n*2)+1) ) :
        if r == 2 or r == 3 or r == 5 or r == 7 :
            M.append(r)
            continue
        if (r % 2) == 0 :
            continue
        for i in range(3,int(r**(1/2)),2):
            if (r % i) == 0 :
                continue
        else : 
            M.append(r)
    return (M)        
print (print_prime_numbers (20))