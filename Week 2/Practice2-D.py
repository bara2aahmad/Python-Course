def states_of_jordan():
    SOJ = ["Irbid" , "Albalqaa", "gerash" , "Alzarqaa", "Altafelah" ," Ajloon" , "Alaqaba" , "Amman" , "Alkerak" , "Madaba", "Maan","Almafreq"]
    print ("the first answer is : ")
    for i in SOJ :
        if i[0] == "A" or i[0] == "a" :
            print (i)
    print (" ")
    print ("the second answer is : ")
    for i in SOJ :
        if len(i) == 5 :
            print (i)

states_of_jordan()