tab = [0] *200
total = 0 
i=0

while(True):
    tab[i] = float(input("Donner une valeur : "))
    if(tab[i]!=-1):
        total += tab[i]
        i+=1
    else:
        break
    
moy = total/i

print(moy)