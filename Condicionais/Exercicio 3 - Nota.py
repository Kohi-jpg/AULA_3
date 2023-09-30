nota1 = float(input('Digite a nota\n'))
nota2 = float(input('Digite a nota\n'))
nota3 = float(input('Digite a nota\n'))

media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f'Você passou com a media de {media}!')
else:
    print(f'Sua nota foi {media}, você está reprovado')