notas=[7,6,6,6]
media=0
for i in range (len(notas)):

    media=notas[i]+media

media_final=media/4

if media_final>=7:
    print(media_final,"aprovado")
else:
    print(media_final,"reprovado")

    