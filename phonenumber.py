# phone number 555-GET-FOOD = 555-438-3663
def PhNum(PhoneNumber):
    Num= PhoneNumber.split('-')
    AreaCode= Num[0]
    NumEnd= Num[1:]
    Number= ''
    for n in NumEnd:
        for i in range (len(n)):
            if n[i] in 'ABC':
                Number= Number+ '2'
            elif n[i] in 'DEF':
                Number= Number+ '3' 
            elif n[i] in 'GHI':
                Number= Number+ '4'
            elif n[i] in 'JKL':
                Number= Number+ '5'
            elif n[i] in 'MNO':
                Number= Number+ '6'
            elif n[i] in 'PQRS':
                Number= Number+ '7'
            elif n[i] in 'TUV':
                Number= Number+ '8'
            elif n[i] in 'WXYZ':
                Number= Number+ '9'
        Number= Number+'-'
    return AreaCode+'-'+Number[:-1]   

PhoneNumber= input("Input Phone Number: ")
NewNumber=PhNum(PhoneNumber)
print(NewNumber)
            
                