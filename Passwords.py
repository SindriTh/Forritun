passw= input('Enter a new password: ')

valid = 0
total = 0
MINIMUM = 6
MAXIMUM = 20

while(passw != "q"):
    litill=0
    stor=0
    tolur=0

    for i in (passw):
        if (97 <= ord(i) <= 122):
            litill += 1
        if (65 <= ord(i) <= 90):
            stor += 1
        if (48 <= ord(i) <= 57):
            tolur += 1

    lengd=litill+stor+tolur

    if MINIMUM<=lengd<=MAXIMUM and litill>0 and stor>0 and tolur>0:
        print('Valid password of length ',lengd)
        valid +=1

    else:
        if (MINIMUM<=lengd<=MAXIMUM) == False:
            print('Invalid length')
        else:
            if (litill>0) == False:
                print('At least one lower case letter needed')
            if (stor>0) == False:
                print('At least one upper case letter needed')
            if (tolur>0) == False:
                print('At least one number needed')

    total += 1
    passw= input('Enter a new password: ')

print("You tried {} passwords, {} valid, {} invalid".format(total,valid,total-valid))
