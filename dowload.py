MB=float(input("tamanho do arquivo:"))
MBS=float(input("velocidade da internet em mbs:"))

MBPS=MB*8
tempo_download=MBPS/MBS
print("tempo de instalação",tempo_download)