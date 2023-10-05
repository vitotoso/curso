nota1=float(input("primeira nota: "))
nota2=float(input("segunda nota: "))
media=(nota1+nota2)/2
print(media)
if media >= 9:
    print("a")
elif media >= 7.5 and media<9:
    print("b")
elif media >=6 and media <7.5:
    print("c")
elif media>= 4 and media<6:
    print("d")
else:
    print("e")

