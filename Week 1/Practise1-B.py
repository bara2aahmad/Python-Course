'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

N = float(input("Enter your Number = "))
if N < -100 :
    print ( -N )
elif N >= -100 and N <= -25 :
    print ( N ** 4 )
elif N > -25 and N <= 0 :
    print ( 3 * ( N ** 2 ) -1 )
elif (N > 0) and (N <= 100) :
    # I had to put the float type before this statment becouse it gave me an error 
    # which was (TypeError: unsupported operand type(s) for +: 'NoneType' and 'int')
    # and I didn't understand why , still thinking it's a stoupid compiler ;)
    print (float ( 90 * N) + float ( 3 ** N)) 
else :
    print (N)