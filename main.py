def askNumber(n):
    return int (input ("Insert the " + str (n) + " Number \n " ))

def returnDivision():
    Result = 0 
    print ("Mathematical Division")
    nNumber = int ( input (" How many numbers do you want to subtract "))
    for  i in range (0, nNumber):
        if i==0:
            Result = askNumber(i+1)
        else:
            Result/= askNumber(i+1)
    return Result

def returnMultiplication():
    Result = 1 
    print ("Multiplication")
    nNumber = int ( input (" How many numbers do you want to subtract "))
    for  i in range (0, nNumber):
        Result*= askNumber(i+1)
    return Result
def returnSum():
    Sum = 0
    print (" Sum " )
    nNumber = int ( input (" How many numbers do you want to sum "))
    for  i in range (0, nNumber):
        Sum += askNumber(i+1)
    return Sum
def returnMinus():
    Result = 0 
    print ("Mathematical Difference ")
    nNumber = int ( input (" How many numbers do you want to subtract "))
    for  i in range (0, nNumber):
        if i==0:
            Result = askNumber(i+1)
        else:
            Result-= askNumber(i+1)
    return Result

def presentation():
    creator="Emanuele Verì"
    pres="Calculator created by {} " 
    print(pres.format(creator))
    
def ask():
    op=["Sum","Difference","Multiplication","Division"]
    for i in range (0, len(op)):
        print ( str(i+1) + " -> " + str(op[i]))
    return int(input("Choose \n"))
    
def main():
    presentation()
    choose = ask()
    if(choose==1):
        print (returnSum())
    elif choose == 2:
        print(returnMinus())
    elif choose == 3 :
        print(returnMultiplication())
    elif choose == 4 :
        print(returnDivision())
    else:
        print(" Non corresponding value ")
main()


