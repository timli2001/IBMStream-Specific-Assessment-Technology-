Read data from input file

allValid = true

def isValid(data,record):
    flag = True
    for i in data:
        if record == i:
            flag = True
        else:
            flag = False
    if flag == True:
        return True
    else:
        return False
errorCodes = []

for each record in input file:
    allValid = record.isValid
    if record.isValid is not true:
        errorCodes.append( "error message")

if allValid is true:
    print ("Yes")
else:
    print ("No")
    print ("false", errorCodes, sep= ' ')