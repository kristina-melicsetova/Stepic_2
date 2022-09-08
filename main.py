predlozhenie = str(input())
n = len(predlozhenie)
slova = 0
for i in range(0,n-1):
    if predlozhenie[i] != ' ' and predlozhenie[i+1] == ' ' :
        slova +=1
 
print(slova +1)

