max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
dollars = 1
days_when_amount_acquired = 0
gotit = False
for i in range(0,max_days+1):
    
    if(dollars >= target):
        gotit = True
        break
    
    dollars += dollars
    days_when_amount_acquired += 1
    
# Ef for lykkjan exitar með break skipuninni og targetið er minna en hámarksupphæð sem hægt er að fá fyrir þann fjölda daga

if gotit and (2**max_days-1 >= target):
    print('Days needed:',days_when_amount_acquired)
else:
    print('Days needed: 0')
    