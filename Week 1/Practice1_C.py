'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
# I have to admit that the idea of the solution wasn't from me 
# but the code is totally mine ;)

print ("this code is a tempreture converter between fahrenheit and Celsius degrees")
Type = input ("choose which unit you will enter , C or F   " )
# I am confused what to name this variable hhhhh
heat_degree = int(input ("enter the heat degree you want to convert  "))

if Type == "C" or Type == "c" :
    Fa = (heat_degree * 9/5 ) + 32 
    print (Fa)
elif Type == "F" or Type == "f" :
    Ce = (heat_degree-32) * 5/9
    print (Ce) 
else :
    print ("re-enter the Type")

