
media=[]
apro=[]
soma=0
for i in range(1,5):
    print("aluno",i)
    
    for a in range(4):
        nota=float(input("insira a nota: "))
        media.append(nota)
        soma=soma+media[a]
    
    media_final=soma/4
    
    print(media_final)
    media_final=0

    if media_final>=7:
        
        apro.append(media_final)
    
    soma=0
    
print(apro)


        
