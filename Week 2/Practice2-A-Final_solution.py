import itertools
M = [ ]
def print_prime_numbers (n) :
    for r in itertools.count():
        if r == 2 or r == 3 or r == 5 or r == 7 :
            M.append(r)
            continue
        if (r % 2) == 0 or (r % 3) == 0 or (r % 5) == 0 or (r % 7) == 0:
            continue
        for i in range(3,int(r**(1/2)+1 ),2):
            if (r % i) == 0 :
                break      
                
        else : 
            M.append(r)
        if len(M) == (n+1) :
            M.remove(1)    
            break
    return (M)        
print (print_prime_numbers (1000))


