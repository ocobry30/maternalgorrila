n = 13
x = 0

series = "sum"

for i in range (0 , n):
    if(series == "fibi"):
        if(i == 0):
            x1= 0
            x2= 0
        elif(i == 1):
            x1 = 1
            x2 = 0
            x = x1 + x2
        else:
            x = x1 + x2
            x2 = x1
            x1 = x
            
    elif(series == "sum"):
         for i in range(0 , n):
             x = 3 * i
             
    else:
        print "invalid, string, loser"  

    print x
