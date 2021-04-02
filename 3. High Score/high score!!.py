Names = []
Names.append('Ben')
Names.append('Thor')
Names.append('Zoe')
Names.append('Kate')
Max = len(Names)-1
Current = 0
Found = False
print ('What player are you looking for?')
PlayerName = input()
while (Found == False) and (Current <= Max):
    if Names[Current] == PlayerName:
        Found = True
    else:
        Current += 1
if Found == True:
    print ('Yes, they have a top score')
else:
    print('No, they do not have a top score')
