nome=input("Nome: ").title()
prova1=float(input("Prova 1: ").replace(",","."))
prova2=float(input("Prova 2: ").replace(",","."))
prova3=float(input("Prova 3: ").replace(",","."))
media=(prova1+prova2+prova3)/3
print("\nResultado:")
print(f"Nome: {nome}")
print(f"Resultado Prova 1: {prova1:.1f}".replace(".",","))
print(f"Resultado Prova 2: {prova2:.1f}".replace(".",","))
print(f"Resultado Prova 3: {prova3:.1f}".replace(".",","))
print(f"Média: {media:.1f}")
if media>=7:
    situacao="aprovado"
elif media>=5:
    situacao="recuperação"
else:
    situacao="reprovado"
print(f"Situação: {situacao.upper()}")