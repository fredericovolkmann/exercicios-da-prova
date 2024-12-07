ingles=['you','and','beautiful','your','hair']
portugues=['voce','é','bonita','seus','cabelos']
tradução=[]
x=input('digite uma palavra ou frase em ingles: ')
P=x.split()
M=[]
for palavra in P:
    if palavra in ingles:
        M.append(portugues[ingles.index(palavra)])
    else:
        M.append(palavra)
print("".join(M))