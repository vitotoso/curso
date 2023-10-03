numeros=[]
numeros_pares=[]
numeros_impares=[]
for i in range(10):
    num = int(input("digite um numero: "))
    numeros.append(num)
  
    if num % 2 == 0:

        numeros_pares.append(num)  
    
    else :
        numeros_impares.append(num)

print(numeros[i])
print("numeros impares",numeros_impares)
print("numeros pares", numeros_pares)