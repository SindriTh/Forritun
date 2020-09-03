max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))

# Fill in the missing code
days_when_amount_acquired = 0
for i in range(0,max_days+1):
    if(2**days_when_amount_acquired <= target):
        days_when_amount_acquired += 1
    
# Ef for lykkjan exitar með break skipuninni og targetið er minna en hámarksupphæð sem hægt er að fá fyrir þann fjölda daga

if (2**max_days-1 >= target):
    print('Days needed:',days_when_amount_acquired)
else:
    print('Days needed: 0')
    