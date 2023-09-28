distancia_da_viagem=float(input("distancia da viagem em km:"))
velocidade=int(input("velocidade media da viagem:"))

horas=int(distancia_da_viagem/velocidade)
tempo_viagem=(distancia_da_viagem/velocidade)*60%60

tempo_viagem=round(tempo_viagem,2)

minutos=tempo_viagem % 60


print("horas",horas,"minutos",minutos)